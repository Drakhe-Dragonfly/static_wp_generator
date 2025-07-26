import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_eq(self):
        node = LeafNode("h", "this is some text")
        node2 = LeafNode("h", "this is some text")
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = LeafNode("p", "dummy text of tests", {"href":"this is not a link..."})
        node2 = LeafNode("p", "dummy text of tests", {"href":"this is not a link..."})
        self.assertEqual(node, node2)

    def test_eq_none(self):
        node = LeafNode(None, None)
        node2 = LeafNode(None, None)
        self.assertEqual(node, node2)