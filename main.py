from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "resume.tex"
OUTPUT_NAME = "akshit_mehta_resume"


def compile_with_tectonic(tectonic: str) -> None:
    subprocess.run(
        [
            tectonic,
            "--outdir",
            str(ROOT),
            SOURCE.name,
        ],
        cwd=ROOT,
        check=True,
    )
    generated_pdf = ROOT / f"{SOURCE.stem}.pdf"
    final_pdf = ROOT / f"{OUTPUT_NAME}.pdf"
    generated_pdf.replace(final_pdf)


def compile_with_pdflatex(pdflatex: str) -> None:
    command = [
        pdflatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-jobname={OUTPUT_NAME}",
        SOURCE.name,
    ]
    for _ in range(2):
        subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    """Compile the LaTeX resume into a consistently named PDF."""
    pdflatex = shutil.which("pdflatex")
    if pdflatex is not None:
        compile_with_pdflatex(pdflatex)
        print(f"Wrote {ROOT / (OUTPUT_NAME + '.pdf')}")
        return

    tectonic = shutil.which("tectonic")
    if tectonic is not None:
        compile_with_tectonic(tectonic)
        print(f"Wrote {ROOT / (OUTPUT_NAME + '.pdf')}")
        return

    sys.exit(
        "No LaTeX engine found. Install TeX Live with `brew install texlive`, "
        "then run `./compile.sh` again."
    )


if __name__ == "__main__":
    main()
