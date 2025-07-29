from enum import Enum
from textnode import TextNode
from textnode import TextType

from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(textnode):
    tag = None
    text = ""
    props = None
    match textnode.text_type:
        case TextType.TEXT: # case for normal text
            text = textnode.text
        case TextType.BOLD: # case for bold text
            tag = "b"
            text = textnode.text
        case TextType.ITALIC: # case for italic text
            tag = "b"
            text = textnode.text
        case TextType.CODE: # case for code blocks
            tag = "code"
            text = textnode.text
        case TextType.LINK: # case for a hyperlink
            tag = "a"
            text = textnode.text
            props = {}
            props["href"] = textnode.url
        case TextType.IMAGE: # case for an image
            tag = "img"
            props = {}
            props["src"] = textnode.url
            props["alt"] = textnode.text
        case _ : # case when the type given is not a correct one
            raise ValueError("invalid node type used")
    
    return LeafNode(tag, text, props)