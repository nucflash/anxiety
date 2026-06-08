#!/usr/bin/env python3
"""
Translate ncase/anxiety localization CSV batches into Greek using local Ollama.

Input CSV columns expected:
  id,path,line,kind,index,source,translation,meta

The script fills only empty translation cells unless --overwrite is passed.
It validates that protected game syntax survives translation.

Requirements:
  - Ollama installed and running: ollama serve
  - A local model pulled, e.g.: ollama pull qwen2.5-coder:32b

Example:
  python translate_anxiety_csv_ollama.py greek_translation_part_01.csv \
    --out greek_translation_part_01.el.csv \
    --model qwen2.5-coder:32b \
    --batch-size 15
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROTECTED_PATTERNS = [
    re.compile(r"`[^`]*`"),              # inline code
    re.compile(r"\{\{[^}]+\}\}"),       # {{variables}}
    re.compile(r"#[A-Za-z0-9_\-]+#"),   # #token# e.g. #pounds#
    re.compile(r"\^[^^]+\^"),           # censorship markers used by the game
]

SYSTEM_PROMPT = """You are translating the game 'Adventures With Anxiety!' into Greek.

Translate ONLY the visible English game text into natural Greek.
Rules:
- Return JSON only, with exactly this shape: {"items":[{"id":"...","translation":"..."}]}.
- Preserve every protected token exactly: inline code in backticks, {{variables}}, #token# markers, markdown emphasis markers, and anchors.
- Preserve markdown formatting: *, **, _, links, line breaks, punctuation that affects rendering.
- Do not translate IDs, anchors, filenames, code, or variables.
- Use informal singular Greek where the text talks to the player.
- Keep the tone playful, emotionally direct, and conversational.
- Prefer concise Greek; avoid bloated literal translations.
- Keep character voice consistency.
- Translate 'Anxiety' as 'Άγχος' when it is the emotion/character; translate 'human' as 'άνθρωπος'.
- Keep profanity intensity roughly equivalent, not stronger.
"""

USER_TEMPLATE = """Translate these CSV rows into Greek. Fill only translation values.

Rows:
{rows_json}
"""

@dataclass
class Row:
    raw: dict[str, str]

    @property
    def id(self) -> str:
        return self.raw["id"]

    @property
    def source(self) -> str:
        return self.raw["source"]

    @property
    def translation(self) -> str:
        return self.raw.get("translation", "") or ""


def protected_items(text: str) -> list[str]:
    items: list[str] = []
    for pat in PROTECTED_PATTERNS:
        items.extend(m.group(0) for m in pat.finditer(text or ""))
    return sorted(items)


def validate_translation(source: str, translation: str) -> list[str]:
    errors: list[str] = []

    src_protected = protected_items(source)
    tr_protected = protected_items(translation)
    if src_protected != tr_protected:
        errors.append(f"protected token mismatch: source={src_protected} translation={tr_protected}")

    if source.count("`") != translation.count("`"):
        errors.append("backtick count mismatch")
    if source.count("{{") != translation.count("{{") or source.count("}}") != translation.count("}}"):
        errors.append("variable brace count mismatch")
    if source.count("*") != translation.count("*"):
        errors.append("markdown asterisk count mismatch")

    src_targets = re.findall(r"\]\((#[^)]+)\)", source)
    tr_targets = re.findall(r"\]\((#[^)]+)\)", translation)
    if src_targets != tr_targets:
        errors.append(f"markdown anchor mismatch: source={src_targets} translation={tr_targets}")

    return errors


def read_csv(path: Path) -> tuple[list[str], list[Row]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = [Row(dict(r)) for r in reader]
    required = {"id", "source", "translation"}
    missing = required - set(fieldnames)
    if missing:
        raise SystemExit(f"Missing required columns: {sorted(missing)}")
    return fieldnames, rows


def write_csv(path: Path, fieldnames: list[str], rows: list[Row]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.raw)


def chunks(xs: list[Row], n: int) -> list[list[Row]]:
    return [xs[i:i+n] for i in range(0, len(xs), n)]


def extract_json_object(text: str) -> dict[str, Any]:
    """Handle models that wrap JSON in fences or add stray text."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


def ollama_generate(
    host: str,
    model: str,
    prompt: str,
    temperature: float,
    timeout_s: int,
) -> str:
    url = host.rstrip("/") + "/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": temperature,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return str(body.get("response", ""))


def call_ollama(
    host: str,
    model: str,
    batch: list[Row],
    max_retries: int = 3,
    temperature: float = 0.2,
    timeout_s: int = 300,
) -> dict[str, str]:
    payload = [
        {
            "id": row.id,
            "kind": row.raw.get("kind", ""),
            "source": row.source,
            "meta": row.raw.get("meta", ""),
        }
        for row in batch
    ]
    prompt = USER_TEMPLATE.format(rows_json=json.dumps(payload, ensure_ascii=False, indent=2))

    for attempt in range(max_retries):
        try:
            text = ollama_generate(host, model, prompt, temperature, timeout_s)
            data = extract_json_object(text)
            items = data.get("items", [])
            return {str(item["id"]): str(item["translation"]) for item in items}
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, TypeError) as e:
            if attempt == max_retries - 1:
                raise
            sleep_s = 2 ** attempt
            print(f"Ollama error: {e}. Retrying in {sleep_s}s...", file=sys.stderr)
            time.sleep(sleep_s)
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--model", default="qwen2.5-coder:32b")
    ap.add_argument("--host", default="http://localhost:11434")
    ap.add_argument("--batch-size", type=int, default=15)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--temperature", type=float, default=0.2)
    ap.add_argument("--timeout", type=int, default=300, help="HTTP timeout per Ollama request in seconds")
    ap.add_argument("--dry-run", action="store_true", help="validate existing translations; do not call Ollama")
    args = ap.parse_args()

    fieldnames, rows = read_csv(args.input_csv)
    todo = [r for r in rows if args.overwrite or not r.translation.strip()]

    print(f"Rows: {len(rows)}; to translate: {len(todo)}")

    if args.dry_run:
        total_errors = 0
        for row in rows:
            if row.translation.strip():
                errors = validate_translation(row.source, row.translation)
                for err in errors:
                    print(f"{row.id}: {err}", file=sys.stderr)
                total_errors += len(errors)
        print(f"Validation errors: {total_errors}")
        return 1 if total_errors else 0

    by_id = {r.id: r for r in rows}
    failures: list[str] = []

    total_batches = (len(todo) + args.batch_size - 1) // args.batch_size
    for i, batch in enumerate(chunks(todo, args.batch_size), start=1):
        print(f"Translating batch {i}/{total_batches} ({len(batch)} rows)")
        try:
            translations = call_ollama(
                host=args.host,
                model=args.model,
                batch=batch,
                temperature=args.temperature,
                timeout_s=args.timeout,
            )
        except Exception as e:
            for row in batch:
                failures.append(f"{row.id}: Ollama call failed: {e}")
            write_csv(args.out, fieldnames, rows)
            continue

        for row in batch:
            tr = translations.get(row.id, "").strip()
            if not tr:
                failures.append(f"{row.id}: missing translation")
                continue
            errors = validate_translation(row.source, tr)
            if errors:
                failures.append(f"{row.id}: " + "; ".join(errors))
                continue
            by_id[row.id].raw["translation"] = tr
            print(tr)

        write_csv(args.out, fieldnames, rows)

    write_csv(args.out, fieldnames, rows)

    if failures:
        fail_path = args.out.with_suffix(".failures.txt")
        fail_path.write_text("\n".join(failures), encoding="utf-8")
        print(f"Finished with {len(failures)} failures. See {fail_path}", file=sys.stderr)
        return 2

    print(f"Wrote {args.out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
