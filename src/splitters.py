from textnode import TextNode, TextType
from extractors import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(node)
            continue

        remaining = text
        for alt, url in matches:
            markdown = f"![{alt}]({url})"
            before, _, after = remaining.partition(markdown)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            continue

        remaining = text
        for anchor, url in matches:
            markdown = f"[{anchor}]({url})"
            before, _, after = remaining.partition(markdown)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            remaining = after

        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))

    return new_nodes
