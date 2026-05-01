import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://example.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            props=None
        )
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "text"})
        rep = repr(node)
        self.assertIn("tag=p", rep)
        self.assertIn("value=Hello", rep)
        self.assertIn("props={'class': 'text'}", rep)


if __name__ == "__main__":
    unittest.main()
