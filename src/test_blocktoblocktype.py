import unittest

from blocktoblocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_bt(self):
        md = """
this is some very long text, with nothing special about it.
Really, there is nothing special, it's not a list, ordered or not.
it's not a code block or a quote, nor is it any headings...
So, yeah, it's just a normal paragraph, without anything weird.
"""
        type_of_block = block_to_block_type(md)
        self.assertEqual(type_of_block, BlockType.PARAGRAPH)

    def test_headings_bt(self):
        md0 = "#this is badly formatted main title (there is a space between the # and the 'this' that's missing)"
        md1 = "# Correctly formatted main title"
        md2 = "## first subtitle size"
        md3 = "### title3, or second subtitle name"
        md4 = "#### It's rare to use a size smaller than this for titles"
        md5 = "##### there is only one title size smaller than this one"
        md6 = "###### this is the smallest title size that can be made.\nIt's also still a little bigger compared to normal text"
        md7 = "####### this is a very smol title, so smol it isn't supported by markdown."
        md_list = [md0, md1, md2, md3, md4, md5, md6, md7]
        md_bt_list = []
        for md in md_list:
            md_bt = block_to_block_type(md)
            md_bt_list.append(md_bt)
        self.assertListEqual([
            BlockType.PARAGRAPH, # md0
            BlockType.HEADING, # md1
            BlockType.HEADING, # md2
            BlockType.HEADING, # md3
            BlockType.HEADING, # md4
            BlockType.HEADING, # md5
            BlockType.HEADING, # md6
            BlockType.PARAGRAPH # md7
            ], md_bt_list)
    
    def test_code_bt(self):
        md = """```def main():
    print("Hello world!") #prints "Hello world!" in the console/terminal
main()```"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)
    
    def test_quote_bt(self):
        md = """>To be or not to be, that is a freaking useless question...
> that's not right, is it?
>no that's wrong, it's not the correct quote"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_unordered_list_bt(self):
        md = """- this is an entry
- and a second one
- and a fourth
- "finishing" by a third."""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_ordered_list_bt(self):
        md = """1. this is the first entry
2. Here is the second one.
3. In here is the third one, in number 3.
4. and here is the entry nb 4 for the last entry"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)