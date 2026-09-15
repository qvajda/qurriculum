"""Uploads generated artifacts to the Cloudflare R2 bucket.

Configuration is the environment, and only the environment: R2_ACCOUNT_ID,
R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET. With none present the
command dry-runs; with a partial set it refuses rather than falling back to a
dry-run, since a half-configured host is the one case where "would have
written..." would be a lie.
"""

import argparse
import os
import sys
from pathlib import Path

import boto3

from qurriculum import generate

TRIO = "be-fr-analytics"

R2_ACCOUNT_ID = "R2_ACCOUNT_ID"
R2_ACCESS_KEY_ID = "R2_ACCESS_KEY_ID"
R2_SECRET_ACCESS_KEY = "R2_SECRET_ACCESS_KEY"
R2_BUCKET = "R2_BUCKET"
REQUIRED_VARS = (R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET)


def key_for(path: Path) -> str:
    return f"artifacts/{TRIO}/{path.name}"


def _present_vars() -> set[str]:
    return {var for var in REQUIRED_VARS if os.environ.get(var)}


def credentials_present() -> bool:
    return _present_vars() == set(REQUIRED_VARS)


def make_client():
    return boto3.client(
        "s3",
        endpoint_url=f"https://{os.environ[R2_ACCOUNT_ID]}.r2.cloudflarestorage.com",
        aws_access_key_id=os.environ[R2_ACCESS_KEY_ID],
        aws_secret_access_key=os.environ[R2_SECRET_ACCESS_KEY],
    )


def upload(paths: list[Path], client=None) -> list[tuple[Path, str]]:
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(path)

    pairs = [(path, key_for(path)) for path in paths]

    if not credentials_present():
        return pairs

    client = client or make_client()
    bucket = os.environ[R2_BUCKET]
    for path, key in pairs:
        client.put_object(Bucket=bucket, Key=key, Body=path.read_bytes())

    return pairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, action="append", dest="artifacts")
    args = parser.parse_args(argv)
    paths = args.artifacts or [generate.DEFAULT_OUT]

    present = _present_vars()
    if present and present != set(REQUIRED_VARS):
        missing = set(REQUIRED_VARS) - present
        print(f"missing credential: {sorted(missing)[0]}", file=sys.stderr)
        return 1

    pairs = upload(paths)
    for _, key in pairs:
        print(key)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
