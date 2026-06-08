#!/usr/bin/env python3
"""Apply index.html translations from greek_translation.csv by html node index."""
from __future__ import annotations

import argparse
import csv
import html
import re
from pathlib import Path

from anxiety_i18n import TextNodeExtractor


def apply_index(repo: Path, rows: list[dict[str, str]]) -> None:
    path = repo / "index.html"
    text = path.read_text(encoding="utf-8")

    by_index: dict[int, str] = {}
    for r in rows:
        if r["kind"] != "html_text" or not r.get("translation", "").strip():
            continue
        by_index[int(r["index"])] = r["translation"]

    parser = TextNodeExtractor()
    parser.feed(text)
    if not by_index:
        return

    # Replace text nodes in reverse order by rebuilding via regex on handle_data sequence
    # Simpler: patch known English strings from source->translation map
    source_to_tr = {
        r["source"]: r["translation"]
        for r in rows
        if r["kind"] == "html_text" and r.get("translation", "").strip()
    }
    for src, tr in sorted(source_to_tr.items(), key=lambda x: -len(x[0])):
        if src in text:
            text = text.replace(src, tr, 1)

    # Meta / title attribute translations
    meta_desc = "Ένα παιχνίδι-ιστορία για έναν άνθρωπο και το άγχος του. Παίζεις ως το άγχος."
    title = "Περιπέτειες με Άγχος!"
    text = re.sub(
        r"(<title>)(.*?)(</title>)",
        rf"\1{title}\3",
        text,
        count=1,
    )
    text = text.replace(
        'content="A story-game about a human and their anxiety. You play as the anxiety."',
        f'content="{meta_desc}"',
    )
    text = text.replace(
        'content="Adventures With Anxiety!"',
        f'content="{title}"',
    )
    text = text.replace(
        "property=\"og:site_name\" content=\"Adventures With Anxiety!\"",
        f'property="og:site_name" content="{title}"',
    )
    text = text.replace("<html>", '<html lang="el">', 1)

    # Add Greek translation link in fan translations list
    if "Ελληνικά" not in text:
        text = text.replace(
            '<a href="https://kyleheren.github.io/anxiety/">한국어</a>',
            '<a href="https://kyleheren.github.io/anxiety/">한국어</a>\n<br>\n<a href="index.html">Ελληνικά</a>',
            1,
        )

    path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="../anxiety-el")
    ap.add_argument("--csv", default="greek_translation.csv")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    with Path(args.csv).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    apply_index(repo, rows)
    print(f"Updated {repo / 'index.html'}")


if __name__ == "__main__":
    main()
