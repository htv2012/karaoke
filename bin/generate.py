#!/usr/bin/env python3
import csv
import pathlib


def create_markdown(row: list[str]) -> str:
    if len(row) == 2:
        terms, author = row
    elif len(row) == 1:
        (terms,) = row
        author = ""
    else:
        raise ValueError(f"Invalid row: {row}")

    terms = terms.split()

    url = f"https://www.youtube.com/results?search_query={'+'.join(terms)}+Karaoke"
    md = f"| [{' '.join(terms)}]({url}) | {author} |\n"
    return md


def generate(source, dest):
    title = " ".join(token.title() for token in source.stem.split("_"))
    with open(source) as ins, open(dest, "w") as outs:
        outs.write(f"# {title}\n\n")
        outs.write("| Title | Writer |\n")
        outs.write("| --- | --- |\n")

        reader = csv.reader(ins)
        for row in reader:
            md = create_markdown(row)
            outs.write(md)


def main():
    """Entry"""
    raw_dir = pathlib.Path(__file__).parent.parent / "raw"
    dest_dir = pathlib.Path(__file__).parent.parent / "karaoke"
    dest_dir.mkdir(exist_ok=True)

    for source in raw_dir.glob("*.txt"):
        dest = dest_dir / f"{source.stem}.md"
        generate(source, dest)


if __name__ == "__main__":
    main()
