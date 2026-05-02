import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_code_split(self):
        node = TextNode("Text `code` more", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

        self.assertEqual(result[2].text, " more")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_no_split_for_non_text_nodes(self):
        bold = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([bold], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], bold)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("Bad `code text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_splits(self):
        node = TextNode("a `x` b `y` c", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        texts = [n.text for n in result]
        types = [n.text_type for n in result]

        self.assertEqual(texts, ["a ", "x", " b ", "y", " c"])
        self.assertEqual(
            types,
            [TextType.TEXT, TextType.CODE,
             TextType.TEXT, TextType.CODE,
             TextType.TEXT]
        )


if __name__ == "__main__":
    unittest.main()
