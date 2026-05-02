import unittest
from textnode import TextNode, TextType
from textnode_to_html import text_node_to_html_node
from leafnode import LeafNode


class TestTextNodeToHTML(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "bold")

    def test_italic(self):
        node = TextNode("italics", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")

    def test_code(self):
        node = TextNode("x = 1", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")

    def test_link(self):
        node = TextNode("Google", TextType.LINK, "https://google.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.props["href"], "https://google.com")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "img.png")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.props["src"], "img.png")
        self.assertEqual(html.props["alt"], "alt text")

    def test_invalid_type(self):
        node = TextNode("text", "INVALID_TYPE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
