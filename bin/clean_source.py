#!/usr/bin/env python3
"""Clean up the source files."""

import csv
import pathlib


def normalize_text(text: str) -> str:
    """Normalize text.

    - Consolidate multiple spaces
    - Title case
    """
    out = (" ".join(text.split())).title()
    return out


def clean(filename: pathlib.Path):
    """Clean up a raw file

    - Remove duplidate
    - Consolidate 
    - Title case
    """
    with open(filename) as stream:
        reader = csv.reader(stream, skipinitialspace=True)
        rows = sorted({tuple(normalize_text(cell) for cell in row) for row in reader})

    with open(filename, "w") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerows(rows)


def main():
    raw_dir = pathlib.Path(__file__).parent.parent / "raw"
    assert raw_dir.is_dir()

    for source in raw_dir.glob("*.txt"):
        clean(source)


if __name__ == "__main__":
    main()
