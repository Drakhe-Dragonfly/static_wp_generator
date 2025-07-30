import unittest
from enum import Enum

from textnode import TextNode
from textnode import TextType

from htmlnode import HTMLNode
from leafnode import LeafNode

from textnode_to_htmlnode import text_node_to_html_node

class TestTNodeToHTMLLeafNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("link to google", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link to google")
        self.assertEqual(html_node.props["href"], "www.google.com")

    def test_image(self):
        node = TextNode("image of the electrostatic cat of wikipedia", "image", "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cat_demonstrating_static_cling_with_styrofoam_peanuts.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "image of the electrostatic cat of wikipedia")
        self.assertEqual(html_node.props["src"], "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cat_demonstrating_static_cling_with_styrofoam_peanuts.jpg")
        
        
if __name__ == "__main__":
    unittest.main()