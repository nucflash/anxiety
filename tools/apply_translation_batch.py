#!/usr/bin/env python3
"""Apply a batch of id->translation mappings to greek_translation.csv."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batch_json", type=Path, help="JSON object: {id: translation, ...}")
    ap.add_argument("--csv", type=Path, default=Path("greek_translation.csv"))
    args = ap.parse_args()

    translations: dict[str, str] = json.loads(args.batch_json.read_text(encoding="utf-8"))
    csv_path = args.csv.resolve()

    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    applied = 0
    for row in rows:
        if row["id"] in translations:
            row["translation"] = translations[row["id"]]
            applied += 1

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Applied {applied}/{len(translations)} translations to {csv_path}")
    missing = set(translations) - {r["id"] for r in rows}
    if missing:
        print(f"WARN: {len(missing)} ids not found in CSV", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
