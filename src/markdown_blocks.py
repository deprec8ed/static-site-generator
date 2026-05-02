def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    cleaned_blocks = []

    for block in raw_blocks:
        stripped = block.strip()

        if stripped:
            cleaned_blocks.append(stripped)

    return cleaned_blocks
