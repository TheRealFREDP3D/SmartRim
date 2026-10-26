import os
import tempfile
import unittest

from smartrim import wiki


class TestWikiPaths(unittest.TestCase):
    def test_raw_dir_is_inside_wiki_dir(self):
        """Raw HTML lives under memory/wiki/raw so .gitignore can cover it."""
        self.assertEqual(os.path.dirname(wiki.RAW_DIR), wiki.WIKI_DIR)
        self.assertTrue(wiki.RAW_DIR.endswith(os.path.join("wiki", "raw")))

    def test_manifest_lives_with_cleaned_pages(self):
        self.assertEqual(os.path.dirname(wiki.MANIFEST_PATH), wiki.WIKI_DIR)

    def test_pages_list_is_populated_and_unique(self):
        self.assertGreater(len(wiki.PAGES), 100)
        self.assertEqual(len(wiki.PAGES), len(set(wiki.PAGES)))

    def test_pages_are_slugs(self):
        for slug in wiki.PAGES:
            self.assertNotIn("/", slug)
            self.assertFalse(slug.startswith("#"))

    def test_no_malformed_slug_with_space(self):
        """A slug containing a space cannot be a valid URL path segment."""
        for slug in wiki.PAGES:
            self.assertNotIn(" ", slug, f"malformed slug: {slug!r}")


class TestStripHtml(unittest.TestCase):
    def test_removes_tags(self):
        out = wiki._strip_html("<p>Hello <b>world</b></p>")
        self.assertIn("Hello", out)
        self.assertIn("world", out)
        self.assertNotIn("<b>", out)

    def test_decodes_entities(self):
        out = wiki._strip_html("<p>Fish &amp; Chips &lt;tags&gt;</p>")
        self.assertIn("Fish & Chips", out)
        self.assertIn("<tags>", out)

    def test_drops_script_and_style_content(self):
        out = wiki._strip_html("<style>body{}</style><script>alert(1)</script><p>Kept</p>")
        self.assertIn("Kept", out)
        self.assertNotIn("alert(1)", out)
        self.assertNotIn("body{}", out)

    def test_lists_become_bullets(self):
        out = wiki._strip_html("<ul><li>one</li><li>two</li></ul>")
        # Bullet marker depends on which converter is installed (html2text vs fallback).
        self.assertIn("one", out)
        self.assertIn("two", out)
        self.assertNotIn("<li>", out)
        self.assertTrue(out.lstrip().startswith(("-", "*")), out[:40])


class TestConvertPages(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.orig_wiki = wiki.WIKI_DIR
        self.orig_raw = wiki.RAW_DIR
        self.orig_manifest = wiki.MANIFEST_PATH
        wiki.WIKI_DIR = os.path.join(self.tmp, "wiki")
        wiki.RAW_DIR = os.path.join(wiki.WIKI_DIR, "raw")
        wiki.MANIFEST_PATH = os.path.join(wiki.WIKI_DIR, "manifest.json")
        os.makedirs(wiki.RAW_DIR, exist_ok=True)

    def tearDown(self):
        wiki.WIKI_DIR = self.orig_wiki
        wiki.RAW_DIR = self.orig_raw
        wiki.MANIFEST_PATH = self.orig_manifest

    def test_convert_writes_markdown_for_each_raw_page(self):
        with open(os.path.join(wiki.RAW_DIR, "Mood.html"), "w", encoding="utf-8") as f:
            f.write("<h1>Mood</h1><p>Colony mood facts.</p>")
        with open(os.path.join(wiki.RAW_DIR, "Other.html"), "w", encoding="utf-8") as f:
            f.write("<p>Other facts.</p>")

        count = wiki.convert_pages()
        self.assertEqual(count, 2)

        md_path = os.path.join(wiki.WIKI_DIR, "Mood.md")
        self.assertTrue(os.path.exists(md_path))
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Mood", content)
        self.assertIn("Colony mood facts.", content)

    def test_convert_skips_non_html_files(self):
        with open(os.path.join(wiki.RAW_DIR, "notes.txt"), "w", encoding="utf-8") as f:
            f.write("ignore me")
        self.assertEqual(wiki.convert_pages(), 0)


class TestManifest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.orig_manifest = wiki.MANIFEST_PATH
        wiki.MANIFEST_PATH = os.path.join(self.tmp, "manifest.json")

    def tearDown(self):
        wiki.MANIFEST_PATH = self.orig_manifest

    def test_missing_manifest_returns_empty(self):
        self.assertEqual(wiki._load_manifest(), {})

    def test_save_and_load_roundtrip(self):
        wiki._save_manifest({"Mood": {"url": "u", "fetched": "2026-10-18", "size": 1}})
        loaded = wiki._load_manifest()
        self.assertIn("Mood", loaded)
        self.assertEqual(loaded["Mood"]["fetched"], "2026-10-18")

    def test_corrupt_manifest_returns_empty(self):
        with open(wiki.MANIFEST_PATH, "w", encoding="utf-8") as f:
            f.write("{not json")
        self.assertEqual(wiki._load_manifest(), {})


if __name__ == "__main__":
    unittest.main()
