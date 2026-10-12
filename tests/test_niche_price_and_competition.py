import pathlib
import re

DOC = pathlib.Path("docs/research/niche-price-and-competition.md")
CONCLUSION = ["PRICE POINT:", "SALES PER MONTH GROSS:", "SALES PER MONTH NET:", "VERDICT:"]


def _text():
    return DOC.read_text(encoding="utf-8")


def test_all_three_trios_present():
    t = _text()
    for trio in ["BE:FR", "DE:DE", "NL:NL"]:
        assert trio in t, f"missing trio: {trio}"


def test_evidence_density():
    t = _text()
    assert len(re.findall(r"https?://", t)) >= 16, "need >=15 listing URLs + Etsy fee page"
    assert len(re.findall(r"\b20\d\d-\d\d-\d\d\b", t)) >= 15, "fewer retrieval dates than listings"
    assert len(set(re.findall(r"etsy\.com/listing/(\d+)", t))) >= 15, "fewer than 15 distinct listings"


def test_conclusion_lines():
    t = _text()
    for line in CONCLUSION:
        assert re.search(rf"^{re.escape(line)}\s*\S", t, re.M), f"missing conclusion line: {line}"
    for line in CONCLUSION[:3]:
        assert re.search(rf"^{re.escape(line)}[^\n]*\d", t, re.M), f"{line} is not a number"


def test_floor_compared():
    assert "175" in _text(), "floor not compared against"
