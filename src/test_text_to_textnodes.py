import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        result = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

    def test_plain_text(self):
        text = "just plain text"
        result = text_to_textnodes(text)

        self.assertEqual(
            result,
            [TextNode("just plain text", TextType.TEXT)]
        )

    def test_only_code(self):
        text = "this has `code` inside"
        result = text_to_textnodes(text)

        self.assertIn(TextNode("code", TextType.CODE), result)

    def test_nested_behavior(self):
        text = "**bold and _italic inside_**"
        result = text_to_textnodes(text)

        self.assertTrue(any(n.text_type == TextType.BOLD for n in result))


if __name__ == "__main__":
    unittest.main()
