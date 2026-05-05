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
REGEN_SCRIPT = REPO_ROOT / "scripts" / "regen.py"


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
    def test_pipeline_round_trips_yaml_and_renders_readme(self):
        """End-to-end: papers.yaml + adjacent.yaml + readme_template/template.md
        in → papers.yaml (re-sorted) + README.md (rendered) out, with no
        intermediate fragment files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "readme_template").mkdir()

            (repo / "readme_template" / "template.md").write_text(
                textwrap.dedent("""\
                Covers **{{insert_paper_count_here}}** papers.

                ## env
                {{insert_env_groups_here}}

                ## keywords
                {{insert_keyword_groups_here}}

                ## authors
                {{insert_author_groups_here}}

                {{insert_paper_list_section_here}}
                """)
            )

            (repo / "papers.yaml").write_text(textwrap.dedent("""\
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
                    @misc{author2026example, title={{Example Paper}}, year={2026} }
                  bibtex_confirmed: false
                """))
            (repo / "adjacent.yaml").write_text("[]\n")
            # Legacy dir that should be cleaned up.
            (repo / "paper_by_env").mkdir()
            (repo / "paper_by_env" / "paper_legacy.md").write_text("legacy")

            with chdir(repo):
                module = load_module("regen_under_test", REGEN_SCRIPT)
                module.process()

            readme = (repo / "README.md").read_text()
            self.assertIn("Covers **1** papers.", readme)
            self.assertIn("Example Paper", readme)
            self.assertNotIn("{{insert_paper_count_here}}", readme)

            # No intermediate fragments are written anymore.
            for f in [
                "paper_count.md", "env_grouping.md", "keyword_grouping.md",
                "author_grouping.md", "paper_list_section.md",
            ]:
                self.assertFalse((repo / "readme_template" / f).exists(),
                                 f"intermediate fragment {f} should not exist")

            # No legacy markdown mirrors.
            self.assertFalse((repo / "ALL_PAPERS.md").exists())
            self.assertFalse((repo / "ADJACENT_PAPERS.md").exists())
            # Legacy paper_by_* dirs cleaned up.
            self.assertFalse((repo / "paper_by_env").exists())


if __name__ == "__main__":
    unittest.main()
