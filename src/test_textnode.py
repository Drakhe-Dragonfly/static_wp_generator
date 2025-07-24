import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif(self):
        node = TextNode("this is a text node", TextType.ITALIC)
        node2 = TextNode("this is another text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_type_dif(self):
        node = TextNode("this is a text node", TextType.ITALIC)
        node2 = TextNode("this is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_edge_case_url(self):
        node = TextNode("that's a link node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("that's a link node", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()