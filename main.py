from pathlib import Path
import argparse
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def compile_with_tectonic(tectonic: str, source: Path, output_name: str) -> None:
    subprocess.run(
        [
            tectonic,
            "--outdir",
            str(ROOT),
            source.name,
        ],
        cwd=ROOT,
        check=True,
    )
    generated_pdf = ROOT / f"{source.stem}.pdf"
    final_pdf = ROOT / f"{output_name}.pdf"
    generated_pdf.replace(final_pdf)


def compile_with_pdflatex(pdflatex: str, source: Path, output_name: str) -> None:
    command = [
        pdflatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-jobname={output_name}",
        source.name,
    ]
    for _ in range(2):
        subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    """Compile the LaTeX resume into a consistently named PDF."""
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="resume.tex")
    parser.add_argument("output_name", nargs="?", default="akshit_mehta_resume")
    args = parser.parse_args()

    source = ROOT / args.source
    if not source.exists():
        sys.exit(f"Source file not found: {source}")

    pdflatex = shutil.which("pdflatex")
    if pdflatex is not None:
        compile_with_pdflatex(pdflatex, source, args.output_name)
        print(f"Wrote {ROOT / (args.output_name + '.pdf')}")
        return

    tectonic = shutil.which("tectonic")
    if tectonic is not None:
        compile_with_tectonic(tectonic, source, args.output_name)
        print(f"Wrote {ROOT / (args.output_name + '.pdf')}")
        return

    sys.exit(
        "No LaTeX engine found. Install TeX Live with `brew install texlive`, "
        "then run `./compile.sh` again."
    )


if __name__ == "__main__":
    main()
