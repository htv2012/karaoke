#!/usr/bin/env python3
import csv
import pathlib

from entry import Entry
from text import normalize_filename


def generate(doc_title: str, entries: list[Entry], dest):
    if not entries:
        return

    with open(dest, "w") as stream:
        stream.write(f"# {doc_title}\n\n")
        stream.write(Entry.md_table_header)

        stream.writelines(entry.as_md_row() for entry in entries)


def main():
    dest_dir = pathlib.Path(__file__).parent.parent / "karaoke"
    dest_dir.mkdir(exist_ok=True)

    with open("raw.csv") as stream:
        reader = csv.reader(stream, skipinitialspace=True)
        entries = [Entry(*row) for row in reader]

    generate("Favorite Karaoke Songs", entries, dest_dir / "all.md")

    # Authors
    authors = set()
    for entry in entries:
        authors.update(entry.authors)
    for author in authors:
        found = [entry for entry in entries if author in entry.authors]
        filename = normalize_filename(author)
        generate(author, found, dest_dir / filename)

    # Tags
    tags = set()
    for entry in entries:
        tags.update(entry.tags)
    for tag in tags:
        found = [entry for entry in entries if tag in entry.tags]
        filename = normalize_filename(tag)
        generate(tag, found, dest_dir / filename)


if __name__ == "__main__":
    main()
