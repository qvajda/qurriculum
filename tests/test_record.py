import sqlite3
from datetime import datetime

import pytest

from qurriculum import ats, generate, record


def test_generation_run_records_one_row_per_artifact(tmp_path):
    out = tmp_path / "fr.docx"
    db = tmp_path / "qurriculum.db"
    generate.render(generate.load_content(), out)
    tier, _, _ = ats.select_tier(out)
    assert ats.check(out) == 0

    record.record_artifact(out, "be:fr:analytics", tier, db)

    conn = sqlite3.connect(db)
    rows = conn.execute(
        "SELECT path, trio, tier, created_at FROM artifacts"
    ).fetchall()
    assert len(rows) == 1
    path, trio, row_tier, created_at = rows[0]
    assert path == str(out)
    assert out.exists()
    assert trio
    assert row_tier
    assert created_at
    datetime.fromisoformat(created_at)


def test_rerunning_does_not_duplicate_the_artifact(tmp_path):
    out = tmp_path / "fr.docx"
    db = tmp_path / "qurriculum.db"
    generate.render(generate.load_content(), out)

    record.record_artifact(out, "be:fr:analytics", "backup", db)
    conn = sqlite3.connect(db)
    first_created_at = conn.execute(
        "SELECT created_at FROM artifacts"
    ).fetchone()[0]

    record.record_artifact(out, "be:fr:analytics", "primary", db)
    rows = conn.execute("SELECT tier, created_at FROM artifacts").fetchall()

    assert len(rows) == 1
    tier, second_created_at = rows[0]
    assert tier == "primary"
    assert second_created_at >= first_created_at


@pytest.mark.parametrize(
    "trio, tier",
    [
        ("", "backup"),
        ("be:fr:analytics", ""),
    ],
)
def test_blank_field_is_refused(tmp_path, trio, tier):
    out = tmp_path / "fr.docx"
    db = tmp_path / "qurriculum.db"
    generate.render(generate.load_content(), out)

    with pytest.raises(sqlite3.IntegrityError):
        record.record_artifact(out, trio, tier, db)

    conn = sqlite3.connect(db)
    conn.execute(record.SCHEMA)
    assert conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0] == 0


def test_missing_artifact_is_refused(tmp_path):
    db = tmp_path / "qurriculum.db"
    missing = tmp_path / "missing.docx"

    with pytest.raises(ValueError):
        record.record_artifact(missing, "be:fr:analytics", "backup", db)

    assert not db.exists()
