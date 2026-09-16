import re

import pytest

from qurriculum import upload

ALL_VARS = upload.REQUIRED_VARS


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for var in ALL_VARS:
        monkeypatch.delenv(var, raising=False)


def test_dry_run_exits_zero_and_prints_the_keys(tmp_path, capsys):
    artifact = tmp_path / "fr.docx"
    artifact.write_bytes(b"content")

    exit_code = upload.main(["--artifact", str(artifact)])

    assert exit_code == 0
    assert f"artifacts/be-fr-analytics/{artifact.name}" in capsys.readouterr().out


def test_key_is_deterministic(tmp_path):
    artifact = tmp_path / "fr.docx"

    first = upload.key_for(artifact)
    second = upload.key_for(artifact)

    assert first == second
    assert not re.search(r"\d{4,}", first)


@pytest.mark.parametrize("missing_var", ALL_VARS)
def test_partial_credentials_are_refused(monkeypatch, tmp_path, capsys, missing_var):
    artifact = tmp_path / "fr.docx"
    artifact.write_bytes(b"content")
    for var in ALL_VARS:
        if var != missing_var:
            monkeypatch.setenv(var, "dummy")

    exit_code = upload.main(["--artifact", str(artifact)])

    assert exit_code != 0
    assert missing_var in capsys.readouterr().err


class _StubClient:
    def __init__(self):
        self.calls = []

    def put_object(self, **kwargs):
        self.calls.append(kwargs)


def test_upload_puts_one_object_per_artifact(monkeypatch, tmp_path):
    for var in ALL_VARS:
        monkeypatch.setenv(var, "dummy")
    monkeypatch.setenv(upload.R2_BUCKET, "my-bucket")
    artifacts = [tmp_path / "a.docx", tmp_path / "b.docx"]
    for artifact in artifacts:
        artifact.write_bytes(b"content")
    client = _StubClient()

    pairs = upload.upload(artifacts, client=client)

    assert len(client.calls) == len(artifacts)
    for call, (path, key) in zip(client.calls, pairs):
        assert call["Bucket"] == "my-bucket"
        assert call["Key"] == key == upload.key_for(path)


def test_upload_failure_is_not_swallowed(monkeypatch, tmp_path):
    for var in ALL_VARS:
        monkeypatch.setenv(var, "dummy")
    artifact = tmp_path / "fr.docx"
    artifact.write_bytes(b"content")

    class _RaisingClient:
        def put_object(self, **kwargs):
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        upload.upload([artifact], client=_RaisingClient())


def test_missing_artifact_is_refused(tmp_path):
    missing = tmp_path / "missing.docx"

    with pytest.raises(FileNotFoundError):
        upload.upload([missing])
