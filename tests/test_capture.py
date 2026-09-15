import os
import shutil

import fitz
import pytest

from qurriculum import capture, generate

no_soffice = pytest.mark.skipif(
    shutil.which("soffice") is None and shutil.which("soffice.exe") is None,
    reason="soffice not installed",
)


@no_soffice
def test_capture_writes_a_nonempty_png_per_page(tmp_path):
    docx_path = tmp_path / "fr.docx"
    generate.render(generate.load_content(), docx_path)
    out_stem = tmp_path / "fr"

    written = capture.capture(docx_path, out_stem)

    assert written
    png_path = written[0]
    assert png_path.stat().st_size > 0

    pix = fitz.Pixmap(str(png_path))
    assert pix.width > 0
    assert pix.height > 0

    samples = {pix.pixel(x, y) for x in range(0, pix.width, max(pix.width // 20, 1))
               for y in range(0, pix.height, max(pix.height // 20, 1))}
    assert len(samples) > 1


def test_renderer_is_present_in_ci():
    if "CI" not in os.environ:
        pytest.skip("not running in CI")
    assert shutil.which("soffice") or shutil.which("soffice.exe")
