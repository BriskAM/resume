# Developer Guide for AI Agents & Developers

This repository is configured in a hybrid public/private architecture to allow hosting a public LaTeX setup while securing personal contact information and domain-specific resumes.

## Architecture Diagram

```mermaid
graph TD
    User([Push to public master]) --> CI[GitHub Actions Runner]
    CI -->|1. Clones using ARCHIVE_PAT| PrivateRepo[Private: resume-archive]
    PrivateRepo -->|2. Pulls templates resume-*.tex| CI
    CI -->|3. Injects Secrets| CompiledLaTeX{All LaTeX Files}
    Secrets[GitHub Secrets] -->|RESUME_EMAIL / PHONE| CompiledLaTeX
    CompiledLaTeX -->|4. Compiles| CompiledPDFs[Compiled PDFs]
    CompiledPDFs -->|5. Pushes PDFs back| PrivateRepo
    CompiledPDFs -->|6. Deploys latest main PDF| GitHubPages[Public: GitHub Pages Website]
```

---

## Repository Roles

1. **Public Repository (`BriskAM/resume`)**
   * **Purpose**: Showcase the build automation code, LaTeX template, and configuration.
   * **Source Files**: `resume.tex` (main resume template, contains contact placeholders).
   * **Git History**: Cleaned and rewritten to ensure no personal email, phone numbers, or PDF files exist in any historical commit.
   * **Website**: GitHub Pages hosts the website which downloads the latest compiled `akshit_mehta_resume.pdf` (built on-the-fly with real details).

2. **Private Repository (`BriskAM/resume-archive`)**
   * **Purpose**: Securely store all domain-specific source files, compiled PDFs with real contact details, and timestamped versions.
   * **Contents**:
     * `resume-cisco.tex` (Cisco resume template, contains contact placeholders).
     * `akshit_mehta_resume_cisco.pdf` (Latest compiled Cisco resume PDF).
     * `versions/akshit-mehta-resume-YYYY-MM-DD-HHMM-sha.pdf` (Dated archive of previous main resume versions).

---

## Secrets Configured (Public Repository)

To edit or update credentials, manage these secrets in the settings of `BriskAM/resume`:
* **`RESUME_EMAIL`**: The email address placed on the compiled resume (e.g. `akshit.mehta.work@gmail.com`).
* **`RESUME_PHONE_DISPLAY`**: The phone number printed on the resume (e.g. `+91 9548783003`).
* **`RESUME_PHONE_LINK`**: The phone number injected into the `tel:` URL (e.g. `+91-9548783003`).
* **`ARCHIVE_PAT`**: A GitHub Personal Access Token (PAT) with write access to `BriskAM/resume-archive` used by the CI/CD runner to clone and push updates.

---

## How to Update Resumes

### Updating the Main Resume (`resume.tex`)
1. Edit `resume.tex` in the public repository.
2. **Crucial**: Ensure any contact details in `resume.tex` remain as placeholders:
   * Email: `email@example.com`
   * Phone link: `+91-0000000000`
   * Phone text: `+91 0000000000`
3. Commit and push to `master`. The workflow will build it with your secrets, deploy the PDF to your public website, and save a backup in the private archive.

### Updating a Domain-Specific Resume (e.g., `resume-cisco.tex`)
Since `resume-cisco.tex` only resides in the private `resume-archive` repository:
1. Clone the private repository `BriskAM/resume-archive`.
2. Edit `resume-cisco.tex` in that repository.
3. Commit and push the changes to `resume-archive`.
4. To build the updated PDF, trigger the workflow in the public repository (e.g., push any minor change or manually trigger the workflow via the GitHub Actions tab). The runner will fetch the updated `.tex` file from your private repository and compile/push the new PDF back.

---

## Local Compilation

To compile resumes locally, ensure you have a LaTeX engine installed (like TeX Live or Tectonic), and run:

```bash
# Compiles main resume
./compile.sh

# Compiles Cisco resume (if copied from your private repository)
python3 main.py resume-cisco.tex akshit_mehta_resume_cisco
```
