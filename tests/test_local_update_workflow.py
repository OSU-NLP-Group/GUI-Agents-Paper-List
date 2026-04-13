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

    def test_process_markdown_creates_general_gui_page_even_when_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "update_template_or_data").mkdir()
            (repo / "paper_by_key").mkdir()
            (repo / "paper_by_env").mkdir()
            (repo / "paper_by_author").mkdir()

            all_papers = textwrap.dedent(
                """\
                - [Example Paper](https://example.com/paper)
                    - Alice Author, Bob Author
                    - 🏛️ Institutions: Example Lab
                    - 📅 Date: March 01, 2026
                    - 📑 Publisher: arXiv
                    - 💻 Env: [Web]
                    - 🔑 Key: [framework], [Example]
                    - 📖 TLDR: Minimal example for testing.
                """
            )
            (repo / "ALL_PAPERS.md").write_text(all_papers)

            with chdir(repo):
                module = load_module("sort_by_date_under_test", SORT_SCRIPT)
                module.process_markdown()

            general_gui_page = repo / "paper_by_env" / "paper_general_gui.md"
            self.assertTrue(general_gui_page.exists())
            self.assertIn("No papers currently tagged with [General GUI].", general_gui_page.read_text())

    def test_process_markdown_removes_legacy_env_pages(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "update_template_or_data").mkdir()
            (repo / "paper_by_key").mkdir()
            env_dir = repo / "paper_by_env"
            env_dir.mkdir()
            (repo / "paper_by_author").mkdir()

            for legacy_name in ("paper_gui.md", "paper_search.md", "paper_misc.md"):
                (env_dir / legacy_name).write_text("legacy")

            all_papers = textwrap.dedent(
                """\
                - [Example Paper](https://example.com/paper)
                    - Alice Author, Bob Author
                    - 🏛️ Institutions: Example Lab
                    - 📅 Date: March 01, 2026
                    - 📑 Publisher: arXiv
                    - 💻 Env: [Web]
                    - 🔑 Key: [framework], [Example]
                    - 📖 TLDR: Minimal example for testing.
                """
            )
            (repo / "ALL_PAPERS.md").write_text(all_papers)

            with chdir(repo):
                module = load_module("sort_by_date_cleanup_under_test", SORT_SCRIPT)
                module.process_markdown()

            self.assertFalse((env_dir / "paper_gui.md").exists())
            self.assertFalse((env_dir / "paper_search.md").exists())
            self.assertFalse((env_dir / "paper_misc.md").exists())


if __name__ == "__main__":
    unittest.main()
