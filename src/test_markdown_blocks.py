import unittest
from markdown_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "Just one paragraph"
        self.assertEqual(
            markdown_to_blocks(md),
            ["Just one paragraph"]
        )

    def test_extra_newlines(self):
        md = "\n\nHello\n\n\nWorld\n\n"
        self.assertEqual(
            markdown_to_blocks(md),
            ["Hello", "World"]
        )

    def test_whitespace_stripping(self):
        md = "   Hello world   \n\n   Second block   "
        self.assertEqual(
            markdown_to_blocks(md),
            ["Hello world", "Second block"]
        )


if __name__ == "__main__":
    unittest.main()
