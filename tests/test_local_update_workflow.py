import importlib.util
import os
import sys
import tempfile
import textwrap
import types
import unittest
from contextlib import contextmanager
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SORT_SCRIPT = REPO_ROOT / "update_template_or_data" / "utils" / "scripts" / "sort_by_date.py"
ASSEMBLE_SCRIPT = REPO_ROOT / "scripts" / "assemble_readme.py"


@contextmanager
def chdir(path: Path):
    previous = Path.cwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(previous)


def load_module(module_name: str, path: Path) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class LocalUpdateWorkflowTests(unittest.TestCase):
    def test_assemble_readme_replaces_placeholders_without_mutating_template(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            update_dir = repo / "update_template_or_data"
            update_dir.mkdir()

            template = textwrap.dedent(
                """\
                Covers **{{insert_paper_count_here}}** papers.
                {{insert_env_groups_here}}
                {{insert_keyword_groups_here}}
                {{insert_author_groups_here}}
                {{insert_paper_list_section_here}}
                After
                """
            )
            (update_dir / "update_readme_template.md").write_text(template)
            (update_dir / "paper_count.md").write_text("42")
            (update_dir / "env_grouping.md").write_text("ENV")
            (update_dir / "keyword_grouping.md").write_text("KEY")
            (update_dir / "author_grouping.md").write_text("AUTHOR")
            (update_dir / "paper_list_section.md").write_text("PAPER_SECTION")

            module = load_module("assemble_readme_under_test", ASSEMBLE_SCRIPT)
            module.assemble_readme(repo)

            readme = (repo / "README.md").read_text()
            self.assertIn("ENV", readme)
            self.assertIn("KEY", readme)
            self.assertIn("AUTHOR", readme)
            self.assertIn("PAPER_SECTION", readme)
            self.assertNotIn("{{insert_env_groups_here}}", readme)
            self.assertEqual((update_dir / "update_readme_template.md").read_text(), template)

    def test_process_round_trips_yaml_and_emits_derived_md(self):
        """The new pipeline reads papers.yaml + adjacent.yaml, emits
        derived ALL_PAPERS.md (no bibtex), generates the README
        fragments, and removes any legacy paper_by_* dirs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "update_template_or_data").mkdir()
            # Legacy dir that should get cleaned up.
            (repo / "paper_by_env").mkdir()
            (repo / "paper_by_env" / "paper_legacy.md").write_text("legacy")

            papers_yaml = textwrap.dedent(
                """\
                - title: Example Paper
                  link: https://example.com/paper
                  authors: [Alice Author, Bob Author]
                  institutions: [Example Lab]
                  date: "2026-03-01"
                  publisher: arXiv
                  envs: [Web]
                  keywords: [framework, Example]
                  tldr: |
                    Minimal example for testing.
                  bibtex: |
                    @misc{author2026example,
                      title = {{Example Paper}},
                      year = {2026}
                    }
                  bibtex_confirmed: false
                """
            )
            (repo / "papers.yaml").write_text(papers_yaml)
            (repo / "adjacent.yaml").write_text("[]\n")

            with chdir(repo):
                module = load_module("sort_by_date_yaml_under_test", SORT_SCRIPT)
                module.process()

            # Derived markdown was emitted, no bibtex inside.
            md = (repo / "ALL_PAPERS.md").read_text()
            self.assertIn("Example Paper", md)
            self.assertIn("- 💻 Env: [Web]", md)
            self.assertNotIn("@misc{", md)

            # Fragments produced.
            self.assertTrue((repo / "update_template_or_data" / "paper_list_section.md").exists())
            self.assertTrue((repo / "update_template_or_data" / "env_grouping.md").exists())

            # Legacy dir cleaned up.
            self.assertFalse((repo / "paper_by_env").exists())


if __name__ == "__main__":
    unittest.main()
