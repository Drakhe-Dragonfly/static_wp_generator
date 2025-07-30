import unittest
from enum import Enum

from textnode import TextNode, TextType

from splitnodedelimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
    ])
    
    def test_emptying_end_nodes(self):
        node = TextNode("*This is text for testing empty nodes*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text for testing empty nodes", TextType.BOLD)])
    
    def test_empty_separator(self):
        node = TextNode("Testing with no delimiters", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], None, TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], " ", TextType.TEXT)
    
    # def


if __name__ == "__main__":
    unittest.main()