#!/usr/bin/env python3
import argparse
import fileinput
import pathlib


def create_markdown(text: str) -> str:
    terms = text.split()
    url = f"https://www.youtube.com/results?search_query={'+'.join(terms)}+Karaoke"
    md = f"- [{' '.join(terms)}]({url})"
    return md


def generate(source, dest):
    title = ' '.join(token.title() for token in source.stem.split("_"))
    with open(source) as ins, open(dest, 'w') as outs:
        outs.write(f"# {title}\n\n")
        for line in ins:
            md = create_markdown(line)
            outs.write(f"{md}\n")

def main():
    """Entry"""
    raw_dir = pathlib.Path(__file__).parent.parent / "raw"
    dest_dir = pathlib.Path(__file__).parent.parent / "karaoke"
    dest_dir.mkdir(exist_ok=True)

    for source in raw_dir.glob("*"):
        dest = dest_dir / f"{source.stem}.md"
        generate(source, dest)



if __name__ == "__main__":
    main()
