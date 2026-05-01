import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click", {"href": "https://google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com">Click</a>'
        )

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_raises_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_repr(self):
        node = LeafNode("span", "hi", {"class": "bold"})
        rep = repr(node)
        self.assertIn("tag=span", rep)
        self.assertIn("value=hi", rep)
        self.assertIn("props={'class': 'bold'}", rep)


if __name__ == "__main__":
    unittest.main()
