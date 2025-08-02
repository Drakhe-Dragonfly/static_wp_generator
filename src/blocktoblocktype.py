from enum import Enum

BlockType = Enum("BlockType", [("PARAGRAPH", "paragraph"), ("HEADING", "heading"), ("CODE", "code"), ("QUOTE", "quote"), ("UNORDERED_LIST", "unordered_list"), ("ORDERED_LIST", "ordered_list")])

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")): # is a heading
        return BlockType.HEADING
    elif block.startswith("```") and (block.removeprefix("```")).endswith("```"): # is a code block
        return BlockType.CODE
    is_quote, is_unordered_list, is_ordered_list = True, True, True
    lined_block = block.split("\n")
    for i in range(len(lined_block)):
        if lined_block[i].startswith(">") == False: # if it's NOT a quote
            is_quote = False
        if lined_block[i].startswith("- ") == False: # if it's NOT an unordered list
            is_unordered_list = False
        if lined_block[i].startswith(f"{i+1}. ") == False: # if it's NOT an ordered list
            is_ordered_list = False
    if is_quote:
        return BlockType.QUOTE
    elif is_unordered_list:
        return BlockType.UNORDERED_LIST
    elif is_ordered_list == True:
        return BlockType.ORDERED_LIST
    else: # is a paragraph
        return BlockType.PARAGRAPH