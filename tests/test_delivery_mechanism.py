import pathlib
import re

DOC = pathlib.Path("docs/research/delivery-mechanism.md")


def _text():
    return DOC.read_text(encoding="utf-8")


def test_limit_lines_present():
    t = _text()
    for label in ["File size:", "File count:", "File types:", "Post-sale replacement:"]:
        assert label in t, f"missing limit line: {label}"


def test_exactly_one_mechanism_line():
    assert len(re.findall(r"^Mechanism:\s*\S", _text(), re.M)) == 1


def test_docx_stated():
    assert ".docx" in _text()


def test_etsy_sources_with_date():
    t = _text()
    etsy = re.findall(r"https?://(?:[\w.-]*\.)?etsy\.com/\S+", t)
    assert len(etsy) >= 4, f"fewer than 4 etsy.com source URLs (found {len(etsy)})"
    assert re.search(r"\b20\d\d-\d\d-\d\d\b", t), "no retrieval date"
