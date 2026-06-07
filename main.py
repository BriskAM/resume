from pathlib import Path
import argparse
import os
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def load_env() -> dict[str, str]:
    env = {}
    env_path = ROOT / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split("=", 1)
                if len(parts) == 2:
                    env[parts[0].strip()] = parts[1].strip()
    return env


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

    # Load secrets from .env file or environment variables
    env = load_env()
    email = env.get("RESUME_EMAIL") or os.environ.get("RESUME_EMAIL")
    phone_link = env.get("RESUME_PHONE_LINK") or os.environ.get("RESUME_PHONE_LINK")
    phone_display = env.get("RESUME_PHONE_DISPLAY") or os.environ.get("RESUME_PHONE_DISPLAY")

    temp_source = None
    if email or phone_link or phone_display:
        print("Injecting secrets into source template...")
        with open(source) as f:
            content = f.read()
        if email:
            content = content.replace("email@example.com", email)
        if phone_link:
            content = content.replace("+91-0000000000", phone_link)
        if phone_display:
            content = content.replace("+91 0000000000", phone_display)

        temp_source = source.parent / f"_temp_{source.name}"
        with open(temp_source, "w") as f:
            f.write(content)
        
        source = temp_source

    try:
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
    finally:
        if temp_source and temp_source.exists():
            print("Cleaning up temporary build files...")
            temp_source.unlink()
            for ext in [".aux", ".log", ".out", ".toc", ".synctex.gz", ".fdb_latexmk", ".fls", ".xdv"]:
                temp_aux = temp_source.parent / f"{temp_source.stem}{ext}"
                if temp_aux.exists():
                    temp_aux.unlink()


if __name__ == "__main__":
    main()
