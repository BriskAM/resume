# Akshit Mehta Resume

LaTeX source and build automation for my resume.

## Download

The latest generated PDF is available at:

- https://briskam.github.io/resume/
- https://briskam.github.io/resume/akshit_mehta_resume.pdf

Older generated PDFs are kept in `versions/` so previous resume revisions can be downloaded from GitHub or from the published version history. The deploy workflow also attempts a Catbox mirror upload with a 30-second timeout.

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

GitHub Actions builds the resume PDF on every push to `master`, archives a dated PDF in `versions/` when the resume content changes, attempts a Catbox mirror upload with a 30-second timeout, and publishes a GitHub Pages site with direct download links.
