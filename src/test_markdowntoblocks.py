import unittest

from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_md_block_stripping(self):
        md = """
   this is **bolded** and padded paragraph         

        This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new     line       

  - This is a list
- with items...
- lots (only 3) items         
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "this is **bolded** and padded paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new     line",
                "- This is a list\n- with items...\n- lots (only 3) items",
            ],
        )
    
    def test_md_with_too_much_lines(self):
        md = """
   this is **bolded** and padded paragraph         

   
        This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new     line       



  - This is a list
- with items...
- lots of items         
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "this is **bolded** and padded paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new     line",
                "- This is a list\n- with items...\n- lots of items",
            ],
        )