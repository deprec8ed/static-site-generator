import re
from block_type import BlockType


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(
        line.split(". ", 1)[0].isdigit()
        for line in lines
    ):
        for i, line in enumerate(lines, start=1):
            if not line.startswith(f"{i}. "):
                break
        else:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
