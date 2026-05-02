import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "italic"),
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold</b> text <i>italic</i></p>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_properties(self):
        child = LeafNode("span", "hi")
        parent = ParentNode(
            "div", [child], {"class": "box", "id": "container"})
        result = parent.to_html()
        valid1 = '<div class="box" id="container"><span>hi</span></div>'
        valid2 = '<div id="container" class="box"><span>hi</span></div>'
        self.assertIn(result, (valid1, valid2))

    def test_missing_tag_raises(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child])

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_empty_children_list(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_repr(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "wrap"})
        rep = repr(parent)
        self.assertIn("tag=div", rep)
        self.assertIn("children=[", rep)
        self.assertIn("props={'class': 'wrap'}", rep)


if __name__ == "__main__":
    unittest.main()
