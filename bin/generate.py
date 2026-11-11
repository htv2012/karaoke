#!/usr/bin/env python3
import csv
import dataclasses
import pathlib


@dataclasses.dataclass
class Entry:
    name: str
    author: str
    tags: str

    md_table_header = "| Name | Author | Tags |\n| --- | --- | --- |\n"

    def as_md_row(self):
        return f"| {self._name} | {self._author} | {self._tags} |\n"

    def split_tags(self) -> list[str]:
        if self.tags == "":
            return []
        return sorted(self.tags.split("|"))

    def tag_match(self, tag: str) -> bool:
        return tag in self.split_tags()

    @property
    def _name(self):
        terms = f"{self.name} Karaoke".split()
        query = "+".join(terms)
        url = f"https://www.youtube.com/results?search_query={query}"
        return self._make_link(self.name, url)

    @property
    def _author(self):
        if self.author == "":
            return ""

        url = f"{self.author.replace(' ', '_').lower()}.md"
        return self._make_link(self.author, url)

    @property
    def _tags(self):
        return " ".join(self._make_tag(tag) for tag in self.split_tags())

    @staticmethod
    def _make_tag(tag: str):
        url = tag.replace(" ", "_") + ".md"
        return Entry._make_link(tag, url)

    @staticmethod
    def _make_link(text: str, url: str) -> str:
        return f"[{text}]({url})"


def generate(doc_title: str, entries: list[Entry], dest):
    if not entries:
        return

    with open(dest, "w") as stream:
        stream.write(f"# {doc_title}\n\n")
        stream.write(Entry.md_table_header)

        stream.writelines(entry.as_md_row() for entry in entries)


def main():
    """Entry"""
    dest_dir = pathlib.Path(__file__).parent.parent / "karaoke"
    dest_dir.mkdir(exist_ok=True)

    with open("raw.txt") as stream:
        reader = csv.reader(stream, skipinitialspace=True)
        entries = [Entry(*row) for row in reader]

    generate("Favorite Karaoke Songs", entries, dest_dir / "all.md")

    # Authors
    authors = {entry.author for entry in entries}
    for author in authors:
        found = [entry for entry in entries if entry.author == author]
        filename = author.replace(" ", "_").lower() + ".md"
        generate(author, found, dest_dir / filename)

    # Tags
    tags = set()
    for entry in entries:
        tags.update(entry.split_tags())
    for tag in tags:
        found = [entry for entry in entries if entry.tag_match(tag)]
        filename = tag.replace(" ", "_") + ".md"
        generate(tag, found, dest_dir / filename)


if __name__ == "__main__":
    main()
