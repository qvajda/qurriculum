"""Records generated artifacts in a local sqlite DB (issue #19).

One row per artifact: path, trio, the ATS tier that passed it, and a
timestamp. The recorder does not run the generator or the ATS gate — it
takes the tier it is given and writes it down.
"""

import argparse
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = Path("out/qurriculum.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS artifacts (
  path       TEXT PRIMARY KEY CHECK (length(path) > 0),
  trio       TEXT NOT NULL    CHECK (length(trio) > 0),
  tier       TEXT NOT NULL    CHECK (length(tier) > 0),
  created_at TEXT NOT NULL    CHECK (length(created_at) > 0)
)
"""


def record_artifact(
    artifact: Path, trio: str, tier: str, db: Path = DEFAULT_DB
) -> None:
    if not artifact.exists():
        raise ValueError(f"artifact does not exist: {artifact}")

    db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db) as conn:
        conn.execute(SCHEMA)
        conn.execute(
            """
            INSERT INTO artifacts (path, trio, tier, created_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT (path) DO UPDATE SET
                trio = excluded.trio,
                tier = excluded.tier,
                created_at = excluded.created_at
            """,
            (
                str(artifact),
                trio,
                tier,
                datetime.now(timezone.utc).isoformat(),
            ),
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--trio", required=True)
    parser.add_argument("--tier", required=True)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    record_artifact(args.artifact, args.trio, args.tier, args.db)


if __name__ == "__main__":
    main()
