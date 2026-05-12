# Akshit Mehta Resume

LaTeX source and build automation for my resume.

## Download

The latest generated PDF is available at:

- https://briskam.github.io/resume/
- https://briskam.github.io/resume/akshit_mehta_resume.pdf

The page also includes a Catbox backup mirror generated during each deployment.

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

GitHub Actions builds the resume PDF on every push to `master`, uploads a fresh Catbox backup mirror, and publishes a GitHub Pages site with direct download links.
