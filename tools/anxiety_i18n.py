#!/usr/bin/env python3
"""
Translation helper for ncase/anxiety.

Usage from the root of your fork:

  python tools/anxiety_i18n.py extract --repo . --out greek_translation.csv
  # fill the translation column
  python tools/anxiety_i18n.py apply --repo . --csv greek_translation.csv --out-dir ../anxiety-el
  python tools/anxiety_i18n.py check --repo ../anxiety-el

What it extracts:
- Markdown dialogue: lines like `h: Hello!`
- Markdown choices: `[Run away](#escape)` -> only `Run away`
- Basic visible text from index.html, excluding script/style/code-ish content

What it preserves:
- section ids beginning with `#`
- choice anchors like `(#escape)`
- inline code in backticks
- `{{variables}}`
- `#pound_tokens#`
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

DIALOGUE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)(:\s*)(.*)$")
CHOICE_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\((#[^)\n]+)\)")
PROTECTED_RE = re.compile(r"(`[^`]*`|\{\{[^}]*\}\}|#[^#\s][^#\n]*#)")
SKIP_HTML_PARENT = {"script", "style", "noscript", "svg", "canvas"}

@dataclass
class Row:
    id: str
    path: str
    line: int
    kind: str
    index: int
    source: str
    translation: str = ""
    meta: str = "{}"


def iter_scene_files(repo: Path) -> Iterable[Path]:
    scenes = repo / "scenes"
    if not scenes.exists():
        raise SystemExit(f"No scenes/ directory found under {repo}")
    yield from sorted(scenes.glob("*.md"))


def extract_markdown(repo: Path) -> list[Row]:
    rows: list[Row] = []
    for path in iter_scene_files(repo):
        rel = path.relative_to(repo).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, start=1):
            stripped = line.lstrip()
            if not stripped or stripped.startswith("#"):
                continue

            m = DIALOGUE_RE.match(line)
            if m and m.group(3).strip():
                text = m.group(3)
                rows.append(Row(
                    id=f"{rel}:{lineno}:dialogue:0",
                    path=rel,
                    line=lineno,
                    kind="dialogue",
                    index=0,
                    source=text,
                    meta=json.dumps({"speaker": m.group(1)}, ensure_ascii=False),
                ))

            for i, cm in enumerate(CHOICE_RE.finditer(line)):
                rows.append(Row(
                    id=f"{rel}:{lineno}:choice:{i}",
                    path=rel,
                    line=lineno,
                    kind="choice",
                    index=i,
                    source=cm.group(1),
                    meta=json.dumps({"anchor": cm.group(2)}, ensure_ascii=False),
                ))
    return rows


class TextNodeExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.stack: list[str] = []
        self.nodes: list[tuple[int, str]] = []
        self.pos = 0

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag.lower())

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.stack[::-1]:
            self.stack.pop()

    def handle_data(self, data):
        self.pos += 1
        if any(t in SKIP_HTML_PARENT for t in self.stack):
            return
        if data.strip() and not data.strip().startswith("<!--"):
            self.nodes.append((self.pos, data))


def extract_index(repo: Path) -> list[Row]:
    path = repo / "index.html"
    if not path.exists():
        return []
    parser = TextNodeExtractor()
    parser.feed(path.read_text(encoding="utf-8"))
    rows: list[Row] = []
    for i, (_, text) in enumerate(parser.nodes):
        clean = html.unescape(text)
        if clean.strip() and len(clean.strip()) <= 500:
            rows.append(Row(
                id=f"index.html:0:html:{i}",
                path="index.html",
                line=0,
                kind="html_text",
                index=i,
                source=clean,
                meta=json.dumps({"html_node_index": i}, ensure_ascii=False),
            ))
    return rows


def write_csv(rows: list[Row], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "path", "line", "kind", "index", "source", "translation", "meta"])
        writer.writeheader()
        for r in rows:
            writer.writerow(r.__dict__)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def protected_tokens(text: str) -> list[str]:
    return PROTECTED_RE.findall(text or "")


def validate_translation(source: str, translation: str, row_id: str) -> list[str]:
    errors = []
    for token in protected_tokens(source):
        if token not in translation:
            errors.append(f"{row_id}: missing protected token in translation: {token}")
    if source.count("^") != translation.count("^"):
        errors.append(f"{row_id}: different number of caret ^ markers; swear-word censoring may break")
    return errors


def copy_repo(repo: Path, out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    ignore = shutil.ignore_patterns(".git", "node_modules", ".DS_Store")
    shutil.copytree(repo, out_dir, ignore=ignore)


def apply_markdown(out_repo: Path, rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_path: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        if r["kind"] in {"dialogue", "choice"} and r.get("translation", "").strip():
            by_path.setdefault(r["path"], []).append(r)

    for rel, file_rows in by_path.items():
        path = out_repo / rel
        lines = path.read_text(encoding="utf-8").splitlines()
        for r in sorted(file_rows, key=lambda x: (int(x["line"]), int(x["index"]))):
            lineno = int(r["line"])
            idx = int(r["index"])
            source = r["source"]
            translation = r["translation"]
            errors.extend(validate_translation(source, translation, r["id"]))
            line = lines[lineno - 1]

            if r["kind"] == "dialogue":
                m = DIALOGUE_RE.match(line)
                if not m:
                    errors.append(f"{r['id']}: dialogue line no longer matches")
                    continue
                lines[lineno - 1] = f"{m.group(1)}{m.group(2)}{translation}"

            elif r["kind"] == "choice":
                matches = list(CHOICE_RE.finditer(line))
                if idx >= len(matches):
                    errors.append(f"{r['id']}: choice index no longer found")
                    continue
                match = matches[idx]
                start, end = match.span(1)
                lines[lineno - 1] = line[:start] + translation + line[end:]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return errors


def check_repo(repo: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_scene_files(repo):
        rel = path.relative_to(repo).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.lstrip().startswith("#"):
                continue
            for cm in CHOICE_RE.finditer(line):
                if not cm.group(2).startswith("#"):
                    errors.append(f"{rel}:{lineno}: choice target is not a section anchor: {cm.group(0)}")
            if line.count("{{") != line.count("}}"):
                errors.append(f"{rel}:{lineno}: unbalanced {{...}} variable braces")
            if line.count("`") % 2 != 0:
                errors.append(f"{rel}:{lineno}: unbalanced backticks")
            if line.count("^") % 2 != 0:
                errors.append(f"{rel}:{lineno}: unbalanced swear-word caret markers")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("extract")
    ex.add_argument("--repo", default=".")
    ex.add_argument("--out", default="greek_translation.csv")
    ex.add_argument("--no-index", action="store_true")

    app = sub.add_parser("apply")
    app.add_argument("--repo", default=".")
    app.add_argument("--csv", required=True)
    app.add_argument("--out-dir", required=True)

    chk = sub.add_parser("check")
    chk.add_argument("--repo", default=".")

    args = ap.parse_args()
    repo = Path(args.repo).resolve()

    if args.cmd == "extract":
        rows = extract_markdown(repo)
        if not args.no_index:
            rows.extend(extract_index(repo))
        write_csv(rows, Path(args.out))
        print(f"Wrote {len(rows)} translatable strings to {args.out}")

    elif args.cmd == "apply":
        out_repo = Path(args.out_dir).resolve()
        copy_repo(repo, out_repo)
        rows = read_csv(Path(args.csv))
        errors = apply_markdown(out_repo, rows)
        if errors:
            print("WARNINGS:")
            for e in errors:
                print("-", e)
        print(f"Wrote translated copy to {out_repo}")

    elif args.cmd == "check":
        errors = check_repo(repo)
        if errors:
            print("CHECK FAILED:")
            for e in errors:
                print("-", e)
            raise SystemExit(1)
        print("OK: no obvious Markdown structure errors found")


if __name__ == "__main__":
    main()
