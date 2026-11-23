import dataclasses

import text


@dataclasses.dataclass
class Entry:
    raw_name: str
    raw_author: str
    raw_tags: str

    md_table_header = "| Name | Author | Tags |\n| --- | --- | --- |\n"

    def __post_init__(self):
        self.authors = self._split(self.raw_author)
        self.tags = self._split(self.raw_tags)

    def as_md_row(self):
        # name
        terms = ["Karaoke"] + self.raw_name.split()
        query = "+".join(terms)
        url = f"https://www.youtube.com/results?search_query={query}"
        name = self.make_link(self.raw_name, url)

        # author
        author = " ".join(self.make_link(author) for author in self.authors)

        # tags
        tags = " ".join(self.make_link(tag) for tag in self.tags)

        return f"| {name} | {author} | {tags} |\n"

    def _split(self, text: str) -> list[str]:
        splitted = sorted(token.strip() for token in text.strip().split("|"))
        if splitted == [""]:
            splitted = []
        return splitted

    def make_link(self, raw_text: str, url=None):
        stripped = text.strip_diacritics(raw_text)
        if url is None:
            url = stripped.replace(" ", "_").lower() + ".md"
        return f"[{raw_text}]({url})"
