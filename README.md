# Akshit Mehta Resume

LaTeX source and build automation for my resume.

## Download

The latest generated PDF is available at:

- https://briskam.github.io/resume/
- https://briskam.github.io/resume/akshit_mehta_resume.pdf

Backup mirror:

- https://files.catbox.moe/peyq2x.pdf

## Build Locally

```sh
./compile.sh
```

The build writes `akshit_mehta_resume.pdf` in the repository root.

## Source Files

- `resume.tex` - resume content and layout
- `main.py` - build script that compiles with `pdflatex`, falling back to `tectonic`
- `compile.sh` - small shell wrapper around `main.py`

## CI/CD

GitHub Actions builds the resume PDF on every push to `master` and publishes a small GitHub Pages site with a direct PDF download link.
