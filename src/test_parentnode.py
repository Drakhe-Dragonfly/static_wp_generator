import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_w_g2childs_n_props(self):
        grandgrandchild_node = LeafNode("b", "grand-grandchild")
        grandgrandchild_node2 = LeafNode("a", "click for me(grand-grandchild n°2)", {"href":"https://www.google.com"})
        grandchild = LeafNode("c", "grandchild leafnode")
        grandchild2 = ParentNode("span", [grandgrandchild_node, grandgrandchild_node2])
        child_node = ParentNode("div2", [grandchild, grandchild2])
        child_node2 = LeafNode("i", "italian child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><div2><c>grandchild leafnode</c><span><b>grand-grandchild</b><a href="https://www.google.com">click for me(grand-grandchild n°2)</a></span></div2><i>italian child</i></div>'
        )

    def test_to_html_empty_child(self):
        child_node = ParentNode("span", [])
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_child_w_none_child(self):
        child_node = ParentNode("span", None)
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_to_html_no_direct_tag(self):
        child_node = ParentNode("span", [])
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_no_indirect_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode(None, [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)