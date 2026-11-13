#!/usr/bin/env python3
"""
Normalize raw.csv
- Make it a real CSV by adding missing author and tags field
"""

import bisect
import csv


def title_word(word: str) -> str:
    """Specialize version of str.title(), which handles Vietnamese words correctly."""
    return word[0].title() + word[1:].lower()


def title_case(text: str) -> str:
    """Handle Vietnamese text, separator (the '|' char)."""
    li = text.split("|")
    out = [" ".join(title_word(word) for word in text.split()) for text in li]
    return "|".join(out)


def normalize_row(row: list[str]) -> tuple[str, str, str]:
    """Normalize a row

    - Ensure it has 3 fields: name, author, and tags
    - Title case the name and author fields
    - Lower case the tags field
    """
    name, author, tags, *_ = row + ["", ""]
    return title_case(name), title_case(author), tags.lower()


def main():
    with open("raw.csv") as stream:
        seen = set()
        rows = []
        reader = csv.reader(stream)

        for row in reader:
            if not row:
                continue

            row = normalize_row(row)
            if row not in seen:
                bisect.insort(rows, row)
            seen.add(row)

    with open("raw.csv", "w") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerows(rows)


if __name__ == "__main__":
    main()
