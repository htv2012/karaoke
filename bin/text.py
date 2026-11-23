#!/usr/bin/env python3
import unicodedata


def strip_diacritics(text: str) -> str:
    """
    Strip diacritics from text, so "Nguyễn Văn Đông" becomes
    "Nguyen Van Dong".
    """
    normalized = unicodedata.normalize("NFD", text)
    without_marks = "".join(
        char for char in normalized if unicodedata.category(char) != "Mn"
    )
    translation_table = str.maketrans({"đ": "d", "Đ": "D"})
    return without_marks.translate(translation_table)


def normalize_filename(text: str) -> str:
    """
    Given text such as "Nguyễn Văn Đông", return
    "nguyen_van_dong.md"
    """
    stripped = strip_diacritics(text)
    return stripped.replace(" ", "_").lower() + ".md"
