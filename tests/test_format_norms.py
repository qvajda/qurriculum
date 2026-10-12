import pathlib
import re

DOC = pathlib.Path("docs/research/format-norms.md")
CLASSES = ["DOCX+PDF", "PDF-ONLY", "LINK", "OTHER", "DOCX"]


def _text():
    return DOC.read_text(encoding="utf-8")


def test_all_three_trios_present():
    t = _text()
    for trio in ["BE:FR", "DE:DE", "NL:NL"]:
        assert trio in t, f"missing trio: {trio}"


def test_evidence_density():
    t = _text()
    assert len(re.findall(r"https?://", t)) >= 15, "fewer listing URLs than listings"
    assert len(re.findall(r"\b20\d\d-\d\d-\d\d\b", t)) >= 15, "fewer retrieval dates than listings"


def test_classes_account_for_fifteen():
    t = _text()
    counts = {}
    for cls in CLASSES:
        m = re.search(rf"^{re.escape(cls)}:\s*(\d+)\s*/\s*15\s*$", t, re.M)
        assert m, f"missing conclusion line: {cls}: <n>/15"
        counts[cls] = int(m.group(1))
    assert sum(counts.values()) == 15, f"classes sum to {sum(counts.values())}, not 15"


def test_verdict_on_d1():
    t = _text()
    v = re.search(r"^VERDICT:\s*(.+)$", t, re.M)
    assert v, "missing VERDICT line"
    assert re.search(r"validates|overturns|no dominant norm", v.group(1)), \
        "VERDICT is not one of validates / overturns / no dominant norm"
    assert "D-1" in t, "D-1 not named"
