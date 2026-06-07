# Akshit Mehta Resume

LaTeX source and build automation for my resume.

## Download

The latest generated PDF is available at:

- https://briskam.github.io/resume/
- https://briskam.github.io/resume/akshit_mehta_resume.pdf

Older generated PDFs, previous resume revisions, and domain-specific resumes are kept in a separate private archive repository for privacy. The deploy workflow also attempts a Catbox mirror upload with a 30-second timeout.

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

GitHub Actions builds the resume PDF on every push to `master`, archives a dated PDF and any domain-specific resumes in a private archive repository, attempts a Catbox mirror upload with a 30-second timeout, and publishes a GitHub Pages site with direct download links.

## Developer Guidelines

For detailed technical guidelines, repository architecture, and instructions on how this public repository integrates with the private archive repository, see [agents.md](agents.md).
