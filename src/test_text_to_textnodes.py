import unittest

from textnode import TextNode, TextType

from splitnodedelimiter import split_nodes_delimiter
from splitnodeimgurl import split_nodes_image, split_nodes_link

from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_one_of_all(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ], new_nodes)
        
    def test_pure_text(self):
        new_nodes = text_to_textnodes("This is text with no italic words and no code blocks and an no obi wan images and a no links")
        self.assertEqual(new_nodes, [TextNode("This is text with no italic words and no code blocks and an no obi wan images and a no links", TextType.TEXT)])
    