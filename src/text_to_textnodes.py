from textnode import TextNode, TextType

from splitnodedelimiter import split_nodes_delimiter
from splitnodeimgurl import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = split_nodes_image([TextNode(text, TextType.TEXT)])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

