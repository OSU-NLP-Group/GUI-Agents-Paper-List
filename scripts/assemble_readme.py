from __future__ import annotations

import argparse
from pathlib import Path


PLACEHOLDERS = {
    "{{insert_env_groups_here}}": "update_template_or_data/env_grouping.md",
    "{{insert_keyword_groups_here}}": "update_template_or_data/keyword_grouping.md",
    "{{insert_author_groups_here}}": "update_template_or_data/author_grouping.md",
    "{{insert_recent_papers_here}}": "update_template_or_data/recent_paper_list.md",
}


def assemble_readme(repo_root: Path) -> Path:
    repo_root = repo_root.resolve()
    template_path = repo_root / "update_template_or_data" / "update_readme_template.md"
    readme_path = repo_root / "README.md"

    rendered = template_path.read_text(encoding="utf-8")
    for placeholder, relative_path in PLACEHOLDERS.items():
        fragment_path = repo_root / relative_path
        fragment = fragment_path.read_text(encoding="utf-8").rstrip("\n")
        rendered = rendered.replace(placeholder, fragment)

    unresolved = [placeholder for placeholder in PLACEHOLDERS if placeholder in rendered]
    if unresolved:
        joined = ", ".join(unresolved)
        raise ValueError(f"README assembly left unresolved placeholders: {joined}")

    readme_path.write_text(rendered.rstrip() + "\n", encoding="utf-8")
    return readme_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble README.md from generated fragments.")
    parser.add_argument(
        "--repo-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Path to the repository root. Defaults to the parent of this script directory.",
    )
    args = parser.parse_args()

    readme_path = assemble_readme(args.repo_root)
    print(f"Wrote {readme_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
