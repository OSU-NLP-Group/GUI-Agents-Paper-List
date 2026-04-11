import importlib.util
import subprocess
import sys
import tempfile
import textwrap
import types
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LINT_SCRIPT = REPO_ROOT / "scripts" / "lint_keys.py"


def load_module(module_name: str, path: Path) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class KeyLintTests(unittest.TestCase):
    def test_write_mode_removes_env_like_keys_and_normalizes_case_family(self):
        module = load_module("lint_keys_under_test", LINT_SCRIPT)
        markdown = textwrap.dedent(
            """\
            - [Paper One](https://example.com/one)
                - Alice Author
                - 🏛️ Institutions: Example Lab
                - 📅 Date: March 01, 2026
                - 📑 Publisher: arXiv
                - 💻 Env: [Web]
                - 🔑 Key: [web], [web agents], [CUAs], [computer-use agents], [Graphical User Interfaces], [browser agents], [mobile GUI agents], [web navigation], [GUI Grounding], [dataset]
                - 📖 TLDR: Example.

            - [Paper Two](https://example.com/two)
                - Bob Author
                - 🏛️ Institutions: Example Lab
                - 📅 Date: March 02, 2026
                - 📑 Publisher: arXiv
                - 💻 Env: [General GUI]
                - 🔑 Key: [GUI grounding], [gui], [benchmark]
                - 📖 TLDR: Example.
            """
        )

        updated_text, issues = module.lint_markdown(markdown, write=True)

        self.assertIn("- 🔑 Key: [GUI grounding], [dataset]", updated_text)
        self.assertIn("- 🔑 Key: [GUI grounding], [benchmark]", updated_text)
        self.assertNotIn("[web]", updated_text)
        self.assertNotIn("[web agents]", updated_text)
        self.assertNotIn("[CUAs]", updated_text)
        self.assertNotIn("[computer-use agents]", updated_text)
        self.assertNotIn("[Graphical User Interfaces]", updated_text)
        self.assertNotIn("[browser agents]", updated_text)
        self.assertNotIn("[mobile GUI agents]", updated_text)
        self.assertNotIn("[web navigation]", updated_text)
        self.assertNotIn("[gui]", updated_text)
        self.assertTrue(any(issue["kind"] == "banned_key" for issue in issues))
        self.assertTrue(any(issue["kind"] == "case_conflict" for issue in issues))

    def test_check_mode_reports_issues_and_exits_non_zero(self):
        markdown = textwrap.dedent(
            """\
            - [Paper One](https://example.com/one)
                - Alice Author
                - 🏛️ Institutions: Example Lab
                - 📅 Date: March 01, 2026
                - 📑 Publisher: arXiv
                - 💻 Env: [Web]
                - 🔑 Key: [web], [CUAs], [computer-use agents], [graphical user interfaces], [browser agents], [mobile GUI agents], [web navigation], [GUI Grounding]
                - 📖 TLDR: Example.

            - [Paper Two](https://example.com/two)
                - Bob Author
                - 🏛️ Institutions: Example Lab
                - 📅 Date: March 02, 2026
                - 📑 Publisher: arXiv
                - 💻 Env: [General GUI]
                - 🔑 Key: [GUI grounding]
                - 📖 TLDR: Example.
            """
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "ALL_PAPERS.md"
            target.write_text(markdown)

            result = subprocess.run(
                [sys.executable, str(LINT_SCRIPT), "--file", str(target)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("banned_key", result.stdout)
        self.assertIn("case_conflict", result.stdout)


if __name__ == "__main__":
    unittest.main()
