#!/usr/bin/env python3
"""Clean up the source files."""

import csv
import pathlib


def title(text: str) -> str:
    tokens = [token.title() for token in text.split()]
    return " ".join(tokens)


def clean(filename: pathlib.Path):
    with open(filename) as stream:
        reader = csv.reader(stream, skipinitialspace=True)
        rows = sorted({tuple(title(cell) for cell in row) for row in reader})

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
