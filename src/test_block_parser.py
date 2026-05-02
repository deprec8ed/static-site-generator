import unittest

from block_parser import block_to_block_type
from block_type import BlockType


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Hello"),
            BlockType.HEADING
        )

        self.assertEqual(
            block_to_block_type("###### Small heading"),
            BlockType.HEADING
        )

    def test_code_block(self):
        block = "```\ncode here\n```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote_block(self):
        block = "> line 1\n> line 2"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_paragraph(self):
        block = "This is just a normal paragraph."
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_mixed_fails_list(self):
        block = "1. first\n3. broken"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()
