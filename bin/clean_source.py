#!/usr/bin/env python3
"""Clean up the source files."""
import pathlib


def title(text: str) -> str:
    tokens = [token.title() for token in text.split()]
    return " ".join(tokens)


def clean(filename: pathlib.Path):
    with open(filename) as stream:
        lines = set(title(line) for line in stream)
        lines = sorted(lines)


    with open(filename, "w") as stream:
        stream.write("\n".join(lines))


def main():
    raw_dir = pathlib.Path(__file__).parent.parent / "raw"
    assert raw_dir.is_dir()

    for source in raw_dir.glob("*"):
        clean(source)


if __name__ == "__main__":
    main()
