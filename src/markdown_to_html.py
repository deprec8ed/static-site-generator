from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from markdown_blocks import markdown_to_blocks
from block_parser import block_to_block_type
from block_type import BlockType
from text_to_textnodes import text_to_textnodes
from textnode_to_html import text_node_to_html_node


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def strip_block_markers(block, block_type):
    lines = block.split("\n")

    if block_type == BlockType.HEADING:
        return lines[0].lstrip("# ").strip()

    if block_type == BlockType.QUOTE:
        return "\n".join(line.lstrip("> ").strip() for line in lines)

    if block_type == BlockType.UNORDERED_LIST:
        return [line.lstrip("- ").strip() for line in lines]

    if block_type == BlockType.ORDERED_LIST:
        return [line.split(". ", 1)[1] for line in lines]

    return block


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            text = block.lstrip("# ").strip()
            level = len(block) - len(block.lstrip("#"))

            tag = f"h{level}"
            children.append(ParentNode(tag, text_to_children(text)))

        elif block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            children.append(
                ParentNode("p", text_to_children(text))
            )

        elif block_type == BlockType.CODE:
            code = block[3:-3].lstrip("\n")
            code_node = LeafNode("code", code)
            pre_node = ParentNode("pre", [code_node])
            children.append(pre_node)

        elif block_type == BlockType.QUOTE:
            text = "\n".join(line.lstrip("> ").strip()
                             for line in block.split("\n"))
            children.append(
                ParentNode("blockquote", text_to_children(text))
            )

        elif block_type == BlockType.UNORDERED_LIST:
            items = [
                ParentNode("li", text_to_children(line.lstrip("- ").strip()))
                for line in block.split("\n")
            ]
            children.append(ParentNode("ul", items))

        elif block_type == BlockType.ORDERED_LIST:
            items = [
                ParentNode("li", text_to_children(line.split(". ", 1)[1]))
                for line in block.split("\n")
            ]
            children.append(ParentNode("ol", items))

    return ParentNode("div", children)
