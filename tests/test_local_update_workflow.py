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
        in → papers.yaml (re-sorted) + README.md (rendered) out, no
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

            with chdir(repo):
                module = load_module("regen_under_test", REGEN_SCRIPT)
                module.process()

            readme = (repo / "README.md").read_text()
            self.assertIn("Covers **1** papers.", readme)
            self.assertIn("Example Paper", readme)
            self.assertNotIn("{{insert_paper_count_here}}", readme)

            # The pipeline writes the README directly — it does not
            # create intermediate fragment files.
            for f in [
                "paper_count.md", "env_grouping.md", "keyword_grouping.md",
                "author_grouping.md", "paper_list_section.md",
            ]:
                self.assertFalse((repo / "readme_template" / f).exists(),
                                 f"intermediate fragment {f} should not exist")


NORMALIZE_SCRIPT = REPO_ROOT / "scripts" / "normalize_institutions.py"


class BibtexGenerationTests(unittest.TestCase):
    """regen.py fills in a BibTeX entry for papers that ship without one."""

    @classmethod
    def setUpClass(cls):
        cls.regen = load_module("regen_bibtex_under_test", REGEN_SCRIPT)

    def test_preprint_becomes_misc_with_eprint(self):
        paper = {
            "title": "VRL-Bench: Benchmarking agents",
            "authors": ["Yu Bai", "Yukai Miao"],
            "date": "2026-09-11",
            "publisher": "arXiv",
            "arxiv_id": "2609.12404",
        }
        entry = self.regen.build_bibtex(paper, set())
        self.assertTrue(entry.startswith("@misc{bai2026vrlbench,"), entry)
        self.assertIn("author = {Yu Bai and Yukai Miao},", entry)
        self.assertIn("eprint = {2609.12404},", entry)
        self.assertIn("archivePrefix = {arXiv},", entry)
        self.assertNotIn("booktitle", entry)

    def test_venue_becomes_inproceedings_without_presentation_qualifier(self):
        paper = {
            "title": "AnchorGUI: Asymmetric Memory",
            "authors": ["Shengjie Jin"],
            "date": "2026-09-14",
            "publisher": "ICLR 2025 (Poster)",
            "arxiv_id": "2609.15457",
        }
        entry = self.regen.build_bibtex(paper, set())
        self.assertTrue(entry.startswith("@inproceedings{jin2026anchorgui,"), entry)
        self.assertIn("booktitle = {ICLR 2025},", entry)

    def test_entry_without_arxiv_id_uses_link(self):
        paper = {
            "title": "Some Paper",
            "authors": ["Ada Lovelace"],
            "date": "2025",
            "publisher": "arXiv",
            "link": "https://example.org/paper",
        }
        entry = self.regen.build_bibtex(paper, set())
        self.assertIn("url = {https://example.org/paper}", entry)
        self.assertNotIn("eprint", entry)

    def test_existing_bibtex_is_never_overwritten(self):
        confirmed = {"title": "T", "authors": ["A B"], "date": "2026",
                     "bibtex": "@inproceedings{handwritten, title={T}}",
                     "bibtex_confirmed": True}
        missing = {"title": "Other Paper", "authors": ["C D"], "date": "2026",
                   "publisher": "arXiv", "arxiv_id": "2601.00001"}
        added = self.regen.fill_bibtex([[confirmed, missing]])
        self.assertEqual(added, 1)
        self.assertEqual(confirmed["bibtex"], "@inproceedings{handwritten, title={T}}")
        self.assertTrue(missing["bibtex"].startswith("@misc{d2026other,"))

    def test_cite_keys_do_not_collide(self):
        papers = [
            {"title": "Same Title", "authors": ["Xu Li"], "date": "2026", "publisher": "arXiv"},
            {"title": "Same Title", "authors": ["Yan Li"], "date": "2026", "publisher": "arXiv"},
            {"title": "Same Title", "authors": ["Zhu Li"], "date": "2026", "publisher": "arXiv"},
        ]
        self.regen.fill_bibtex([papers])
        keys = [p["bibtex"].split("{", 1)[1].split(",", 1)[0] for p in papers]
        self.assertEqual(len(set(keys)), 3, keys)

    def test_existing_keys_are_reserved_before_generating(self):
        papers = [
            {"title": "Same Title", "authors": ["Xu Li"], "date": "2026",
             "bibtex": "@misc{li2026same, title={Same Title}}"},
            {"title": "Same Title", "authors": ["Yan Li"], "date": "2026", "publisher": "arXiv"},
        ]
        self.regen.fill_bibtex([papers])
        self.assertNotIn("@misc{li2026same,", papers[1]["bibtex"])


class InstitutionNormalizationTests(unittest.TestCase):
    """The institution pass rewrites only names it recognises."""

    @classmethod
    def setUpClass(cls):
        cls.ni = load_module("normalize_under_test", NORMALIZE_SCRIPT)

    def test_known_names_are_canonicalised(self):
        self.assertEqual(
            self.ni.normalize_entry(
                ["Zhejiang University", "Tsinghua University", "Johns Hopkins University"]
            ),
            ["ZJU", "Tsinghua", "JHU"],
        )

    def test_unknown_names_pass_through_untouched(self):
        names = ["Paderborn University", "Coasty Research Lab", "Aether AI"]
        self.assertEqual(self.ni.normalize_entry(names), names)

    def test_comma_containing_name_is_kept_whole(self):
        for name in [
            "Institute of Software, Chinese Academy of Sciences",
            "DAMO Academy, Alibaba Group",
            "Ningxia Electric Power Engineering Co., Ltd.",
        ]:
            self.assertEqual(self.ni.normalize_entry([name]), [name])

    def test_adjacent_pair_naming_one_institution_is_merged(self):
        self.assertEqual(
            self.ni.normalize_entry(["University of California", "Berkeley"]),
            ["UC Berkeley"],
        )
        self.assertEqual(
            self.ni.normalize_entry(["The Chinese University of Hong Kong", "Shenzhen"]),
            ["CUHK-Shenzhen"],
        )

    def test_the_prefix_is_stripped_only_when_a_rule_matches(self):
        self.assertEqual(self.ni.normalize_entry(["The Ohio State University"]), ["OSU"])
        self.assertEqual(
            self.ni.normalize_entry(["The University of Tokyo"]), ["The University of Tokyo"]
        )

    def test_company_and_its_research_division_stay_distinct(self):
        self.assertEqual(
            self.ni.normalize_entry(["Google", "Google Research", "IBM", "IBM Research"]),
            ["Google", "Google Research", "IBM", "IBM Research"],
        )

    def test_preexisting_duplicates_are_preserved(self):
        names = ["Indian Institute of Technology", "Bombay",
                 "Indian Institute of Technology", "Hyderabad"]
        self.assertEqual(self.ni.normalize_entry(names), names)

    def test_duplicates_created_by_mapping_are_collapsed(self):
        self.assertEqual(
            self.ni.normalize_entry(["Tsinghua", "Tsinghua University"]), ["Tsinghua"]
        )

    def test_is_idempotent(self):
        names = ["Zhejiang University", "University of California", "Berkeley",
                 "The University of Tokyo", "DAMO Academy, Alibaba Group"]
        once = self.ni.normalize_entry(names)
        self.assertEqual(self.ni.normalize_entry(once), once)

if __name__ == "__main__":
    unittest.main()
