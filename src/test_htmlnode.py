import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('header', 'this is some text', ['falsenode'], {'what':'question', "hey don't look at this entry":'entry'})
        node2 = HTMLNode('header', 'this is some text', ['falsenode'], {'what':'question', "hey don't look at this entry":'entry'})
        self.assertEqual(node, node2)

    def test_eq_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_diff(self):
        node = HTMLNode("header", "this is some text", ["dummynode1", "dummynode2", "dummynode3"])
        node2 = HTMLNode("body text", "this is some other text", [node], {"prop1":"thing", "prop2":"other thing"})
        self.assertNotEqual(node, node2)

    def test_eq_none_props_to_html(self):
        node = HTMLNode("test_tag")
        node2 = HTMLNode("test_tag")
        node_result = node.props_to_html()
        node2_result = node2.props_to_html()
        self.assertEqual(node_result, node2_result)

    def test_eq_props_to_html(self):
        node = HTMLNode("body text", "this is some other text", ["node"], {"prop1":"thing", "prop2":"other thing"})
        node2 = HTMLNode("body text", "this is some other text", ["node"], {"prop1":"thing", "prop2":"other thing"})
        node_result = node.props_to_html()
        node2_result = node2.props_to_html()
        self.assertEqual(node_result, node2_result)
        
        
if __name__ == "__main__":
    unittest.main()