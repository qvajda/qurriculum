import copy

import docx
import pytest

from qurriculum import ats, generate


def test_tier_is_always_printed(tmp_path, capsys):
    out = tmp_path / "fr.docx"
    generate.render(generate.load_content(), out)

    ats.check(out)

    first_line = capsys.readouterr().out.splitlines()[0]
    assert first_line.startswith("tier=")


def test_green_on_generated_fr_core(tmp_path, capsys):
    out = tmp_path / "fr.docx"
    generate.render(generate.load_content(), out)

    exit_code = ats.check(out)

    output = capsys.readouterr().out
    assert exit_code == 0
    first_line = output.splitlines()[0]
    tier = first_line.removeprefix("tier=").split()[0]
    assert tier in {"primary", "backup"}


def _drop_email(content):
    content["contact"] = [
        line for line in content["contact"] if "@" not in line
    ]


def _drop_phone(content):
    content["contact"] = [
        line for line in content["contact"] if not line.startswith("+")
    ]


def _drop_name(content):
    content["name"] = ""


def _drop_heading(heading):
    def _drop(content):
        content["sections"] = [
            s for s in content["sections"] if s["heading"] != heading
        ]

    return _drop


@pytest.mark.parametrize(
    "field, mutate",
    [
        ("email", _drop_email),
        ("phone", _drop_phone),
        ("name", _drop_name),
        ("Formation", _drop_heading("Formation")),
        ("Expérience professionnelle", _drop_heading("Expérience professionnelle")),
    ],
)
def test_red_on_missing_required_field(tmp_path, capsys, field, mutate):
    content = copy.deepcopy(generate.load_content())
    mutate(content)
    out = tmp_path / "fr.docx"
    generate.render(content, out)

    exit_code = ats.check(out)

    output = capsys.readouterr().out
    assert exit_code == 1
    assert f"{field}: missing" in output


def test_unreadable_file_exits_two(tmp_path, capsys):
    out = tmp_path / "not-a-docx.docx"
    out.write_text("not a docx file")

    exit_code = ats.check(out)

    assert exit_code == 2
