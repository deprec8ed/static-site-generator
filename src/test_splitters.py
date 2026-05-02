import unittest
from textnode import TextNode, TextType
from splitters import split_nodes_image, split_nodes_link


class TestSplitters(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE,
                         "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_none(self):
        node = TextNode("No images here", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links(self):
        node = TextNode(
            "Click [here](https://x.com) or [there](https://y.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Click ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://x.com"),
                TextNode(" or ", TextType.TEXT),
                TextNode("there", TextType.LINK, "https://y.com"),
            ],
            new_nodes,
        )

    def test_split_links_none(self):
        node = TextNode("Just text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_link_mixed_nodes(self):
        nodes = [
            TextNode("Look at ", TextType.TEXT),
            TextNode("ignored", TextType.BOLD),
        ]

        out = split_nodes_link(nodes)
        self.assertEqual(nodes, out)


if __name__ == "__main__":
    unittest.main()
