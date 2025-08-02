
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    temp_blocks = []
    for block in blocks:
        temp_blocks.append((block.strip()).strip("\n"))
    blocks = temp_blocks.copy()
    temp_blocks = []
    for block in blocks:
        if block != "" and block != "\n" and block != '' and len(block) != 0:
            temp_blocks.append(block)
    blocks = temp_blocks
    #print(blocks)
    return blocks