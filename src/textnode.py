from enum import Enum

TextType = Enum("TextType", [("PLAIN", "plain"), ("BOLD", "bold"), ("ITALIC", "italic"), ("CODE", "code"), ("LINK", "link"), ("IMAGE", "image")])

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, textnode):
        return self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
