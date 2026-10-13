"""Fills the contact placeholders in the LaTeX templates during CI.

The public resume (resume.tex) is published on GitHub Pages, mirrored to other hosts and indexed by scrapers, so it is
built WITHOUT a phone number: the phone entry is removed from its header and only the email is injected. Private
variants (from the archive repository) keep the phone number. Local builds through main.py are unaffected.
"""
import glob
import os
import re

PHONE_ENTRY = re.compile(
    r"[ \t]*\\mbox\{\\hrefWithoutArrow\{tel:\+91-0000000000\}\{\+91 0000000000\}\}%\n"
    r"(?:[ \t]*\\kern 0\.15 cm%\n[ \t]*\\AND%\n[ \t]*\\kern 0\.15 cm%\n)?"
)
PUBLIC_TEMPLATES = {"resume.tex"}


def main() -> None:
    email = os.environ["RESUME_EMAIL"]
    phone_link = os.environ.get("RESUME_PHONE_LINK", "")
    phone_display = os.environ.get("RESUME_PHONE_DISPLAY", "")
    for path in glob.glob("*.tex"):
        content = open(path).read()
        if path in PUBLIC_TEMPLATES:
            content, removed = PHONE_ENTRY.subn("", content)
            if "+91 0000000000" in content or "+91-0000000000" in content:
                raise SystemExit(f"{path}: phone placeholder is still present after stripping; refusing to publish")
            print(f"{path}: public build, phone entry removed ({removed})")
        else:
            content = content.replace("+91-0000000000", phone_link).replace("+91 0000000000", phone_display)
        content = content.replace("email@example.com", email)
        open(path, "w").write(content)


if __name__ == "__main__":
    main()
