"""Renders a .docx to PNGs (one per page) via LibreOffice + PyMuPDF.

`soffice --convert-to png` is one step shorter but emits page 1 only; a PDF
intermediate is required to get every page and to assert the page count.
"""

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz

DEFAULT_DOCX = Path("out/be-fr-analytics-fr.docx")
DEFAULT_OUT_STEM = Path("out/be-fr-analytics-fr")


def find_renderer() -> str:
    renderer = shutil.which("soffice") or shutil.which("soffice.exe")
    if renderer is None:
        raise SystemExit("capture: soffice not found on PATH")
    return renderer


def capture(docx_path: Path, out_stem: Path) -> list[Path]:
    renderer = find_renderer()
    out_stem.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            [renderer, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(docx_path)],
            check=True,
        )
        pdf_path = Path(tmp) / (docx_path.stem + ".pdf")
        written = []
        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                png_path = out_stem.parent / f"{out_stem.name}-p{page.number + 1}.png"
                page.get_pixmap().save(png_path)
                written.append(png_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", type=Path, default=DEFAULT_DOCX)
    parser.add_argument("--out-stem", type=Path, default=DEFAULT_OUT_STEM)
    args = parser.parse_args()
    capture(args.docx, args.out_stem)


if __name__ == "__main__":
    main()
