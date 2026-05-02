import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_simple_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_title_with_whitespace(self):
        md = "   #   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_multiline_title(self):
        md = """
# Main Title

Some text here
"""
        self.assertEqual(extract_title(md), "Main Title")

    def test_missing_title_raises(self):
        md = "## Not an h1"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
