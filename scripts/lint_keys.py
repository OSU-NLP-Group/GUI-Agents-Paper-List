#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


TITLE_LINE_RE = re.compile(r"^- \[(?P<title>.*?)\]\((?P<link>.*?)\)$")
KEY_LINE_RE = re.compile(r"^(?P<prefix>\s*-\s*🔑 Key:\s*)(?P<body>.*?)(?P<suffix>\s*)$")
KEY_TOKEN_RE = re.compile(r"\[(.*?)\]")

BANNED_KEY_FAMILIES = {
    "web",
    "mobile",
    "desktop",
    "gui",
    "search",
    "cua",
    "cuas",
    "computer-use agent",
    "computer-use agents",
    "computer use agent",
    "computer use agents",
    "computer-using agent",
    "computer-using agents",
    "computer using agent",
    "computer using agents",
    "graphical user interface",
    "graphical user interfaces",
    "web navigation",
    "browser agent",
    "browser agents",
    "mobile gui agent",
    "mobile gui agents",
    "web agent",
    "web agents",
    "mobile agent",
    "mobile agents",
    "desktop agent",
    "desktop agents",
    "gui agent",
    "gui agents",
}


def normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def family_key(value: str) -> str:
    return normalize_whitespace(value).casefold()


def parse_key_tokens(body: str) -> list[str]:
    return [normalize_whitespace(match.group(1)) for match in KEY_TOKEN_RE.finditer(body)]


def is_preferred_phrase_form(value: str) -> bool:
    tokens = value.split()
    if len(tokens) < 2:
        return False

    saw_lowercase_word = False
    for token in tokens:
        letters = "".join(character for character in token if character.isalpha())
        if not letters:
            continue
        if letters.isupper() and len(letters) >= 2:
            continue
        if letters.islower():
            saw_lowercase_word = True
            continue
        return False
    return saw_lowercase_word


def is_mixed_case_single_token(value: str) -> bool:
    if " " in value:
        return False
    return any(character.islower() for character in value) and any(character.isupper() for character in value[1:])


def canonical_sort_key(value: str, count: int) -> tuple[object, ...]:
    return (
        -count,
        0 if is_preferred_phrase_form(value) else 1,
        0 if is_mixed_case_single_token(value) else 1,
        value.casefold(),
        value,
    )


def choose_canonical_form(counter: Counter[str]) -> str:
    return min(counter.items(), key=lambda item: canonical_sort_key(item[0], item[1]))[0]


def build_canonical_map(lines: list[str]) -> dict[str, str]:
    families: dict[str, Counter[str]] = defaultdict(Counter)
    for line in lines:
        match = KEY_LINE_RE.match(line)
        if not match:
            continue
        for token in parse_key_tokens(match.group("body")):
            family = family_key(token)
            if family in BANNED_KEY_FAMILIES:
                continue
            families[family][token] += 1

    return {family: choose_canonical_form(counter) for family, counter in families.items()}


def lint_markdown(markdown: str, write: bool = False) -> tuple[str, list[dict[str, object]]]:
    lines = markdown.splitlines()
    canonical_map = build_canonical_map(lines)
    issues: list[dict[str, object]] = []
    updated_lines: list[str] = []
    current_title = ""

    for line_number, line in enumerate(lines, start=1):
        title_match = TITLE_LINE_RE.match(line)
        if title_match:
            current_title = title_match.group("title")

        key_match = KEY_LINE_RE.match(line)
        if not key_match:
            updated_lines.append(line)
            continue

        updated_tokens: list[str] = []
        seen_families: set[str] = set()
        for token in parse_key_tokens(key_match.group("body")):
            family = family_key(token)
            if family in BANNED_KEY_FAMILIES:
                issues.append(
                    {
                        "kind": "banned_key",
                        "line": line_number,
                        "title": current_title,
                        "key": token,
                    }
                )
                continue

            canonical = canonical_map.get(family, token)
            if canonical != token:
                issues.append(
                    {
                        "kind": "case_conflict",
                        "line": line_number,
                        "title": current_title,
                        "key": token,
                        "canonical": canonical,
                    }
                )

            if family in seen_families:
                issues.append(
                    {
                        "kind": "duplicate_key_family",
                        "line": line_number,
                        "title": current_title,
                        "key": canonical,
                    }
                )
                continue

            seen_families.add(family)
            updated_tokens.append(canonical)

        if write:
            updated_body = ", ".join(f"[{token}]" for token in updated_tokens)
            updated_lines.append(f"{key_match.group('prefix')}{updated_body}")
        else:
            updated_lines.append(line)

    updated_text = "\n".join(updated_lines)
    if markdown.endswith("\n"):
        updated_text += "\n"
    return updated_text, issues


def format_issue(issue: dict[str, object]) -> str:
    base = f"{issue['kind']}: {issue['title']} (line {issue['line']})"
    if issue["kind"] == "banned_key":
        return f"{base} -> [{issue['key']}]"
    if issue["kind"] == "case_conflict":
        return f"{base} -> [{issue['key']}] should be [{issue['canonical']}]"
    return f"{base} -> [{issue['key']}]"


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint and optionally rewrite Key fields in ALL_PAPERS.md.")
    parser.add_argument(
        "--file",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "ALL_PAPERS.md",
        help="Markdown file to lint.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Rewrite the file to remove banned keys and normalize case families.",
    )
    args = parser.parse_args()

    markdown = args.file.read_text()
    updated_text, issues = lint_markdown(markdown, write=args.write)

    if args.write and updated_text != markdown:
        args.file.write_text(updated_text)

    if issues:
        for issue in issues:
            print(format_issue(issue))
        print(f"\nFound {len(issues)} key issue(s).")
        return 0 if args.write else 1

    print("No key issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
