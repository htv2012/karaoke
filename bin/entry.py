import dataclasses
import io


@dataclasses.dataclass
class Entry:
    raw_name: str
    raw_author: str
    raw_tags: str

    md_table_header = "| Name | Author | Tags |\n| --- | --- | --- |\n"

    def as_md_row(self):
        return f"| {self._name} | {self._author} | {self._tags} |\n"

    def as_book_entry(self):
        buf = io.StringIO()
        buf.write(f"\n### {self._name}\n")
        if self.authors:
            s = "s" if len(self.authors) > 1 else ""
            buf.write(f"- Author{s}: ")
            buf.write(", ".join(f"[{author}]" for author in self.authors))
            buf.write("\n")

        if self.tags:
            s = "s" if len(self.tags) > 1 else ""
            buf.write(f"- Tags{s}: ")
            buf.write(", ".join(f"- [{tag}]" for tag in self.tags))
            buf.write("\n")

        return buf.getvalue()

    @property
    def tags(self) -> list[str]:
        return self._split(self.raw_tags)

    @property
    def authors(self) -> list[str]:
        return self._split(self.raw_author)

    def tag_match(self, tag: str) -> bool:
        return tag in self.tags

    def author_match(self, author: str) -> bool:
        return author in self.authors

    @property
    def _name(self):
        terms = f"Karaoke {self.raw_name}".split()
        query = "+".join(terms)
        url = f"https://www.youtube.com/results?search_query={query}"
        return self.make_link(self.raw_name, url)

    @property
    def _author(self):
        return " ".join(self.make_link(author) for author in self.authors)

    @property
    def _tags(self):
        return " ".join(self.make_link(tag) for tag in self.tags)

    def _split(self, text: str) -> list[str]:
        if text == "":
            return []
        return sorted(text.split("|"))

    @staticmethod
    def make_link(text: str, url=None):
        if url is None:
            url = text.replace(" ", "_").lower() + ".md"
        return f"[{text}]({url})"
