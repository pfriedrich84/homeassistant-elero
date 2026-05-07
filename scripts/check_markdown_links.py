#!/usr/bin/env python3
"""Check local links in Markdown files.

The checker is intentionally dependency-free. It skips external URLs, mailto links,
and generated/dependency directories, then verifies that local relative links point
to existing files/directories and that simple heading anchors exist.
"""

from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def slugify(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = heading.strip().lower()
    heading = re.sub(r"[`*_]", "", heading)
    heading = re.sub(r"[^a-z0-9\s-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading.strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(errors="ignore")
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            anchors.add(slugify(match.group(2)))
    return anchors


def is_external_or_special(target: str) -> bool:
    parsed = urllib.parse.urlsplit(target)
    if parsed.scheme in EXTERNAL_SCHEMES:
        return True
    return target.startswith(("#", "mailto:"))


def resolve_target(source: Path, raw_target: str) -> tuple[Path, str]:
    parsed = urllib.parse.urlsplit(raw_target)
    unquoted_path = urllib.parse.unquote(parsed.path)
    target_path = (source.parent / unquoted_path).resolve()
    return target_path, urllib.parse.unquote(parsed.fragment)


def main() -> int:
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}

    for md_file in iter_markdown_files():
        text = md_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(2).strip()
            if is_external_or_special(raw_target):
                continue

            target_path, fragment = resolve_target(md_file, raw_target)
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{md_file.relative_to(ROOT)}: link escapes repository: {raw_target}")
                continue

            if not target_path.exists():
                errors.append(f"{md_file.relative_to(ROOT)}: missing target: {raw_target}")
                continue

            if fragment and target_path.is_file() and target_path.suffix.lower() == ".md":
                anchors = anchor_cache.setdefault(target_path, anchors_for(target_path))
                if fragment.lower() not in anchors:
                    errors.append(
                        f"{md_file.relative_to(ROOT)}: missing anchor #{fragment} in "
                        f"{target_path.relative_to(ROOT)}"
                    )

    if errors:
        print("Broken Markdown links:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Markdown links OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
