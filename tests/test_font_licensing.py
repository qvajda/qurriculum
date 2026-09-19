import re
import pathlib

DOC = pathlib.Path("docs/research/font-licensing.md")
FAMILIES = ["Aptos", "Calibri", "Cambria", "Arial", "Times New Roman", "Georgia",
            "EB Garamond", "Lato"]


def _text():
    return DOC.read_text(encoding="utf-8")


def test_every_family_named():
    for f in FAMILIES:
        assert f in _text(), f"missing family: {f}"


def test_source_url_per_family():
    assert len(re.findall(r"https?://", _text())) >= len(FAMILIES)


def test_retrieval_date():
    assert re.search(r"\b20\d\d-\d\d-\d\d\b", _text())


def test_quoted_clauses():
    assert _text().count(">") >= len(FAMILIES)


def test_conclusion_lists():
    t = _text()
    assert "MAY EMBED:" in t and "MAY DEPEND ON, MUST NOT EMBED:" in t
