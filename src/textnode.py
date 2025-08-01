from enum import Enum

TextType = Enum("TextType", [("TEXT", "text"), ("BOLD", "bold"), ("ITALIC", "italic"), ("CODE", "code"), ("LINK", "link"), ("IMAGE", "image")])

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        if text_type is TextType:
            self.text_type = text_type
        else:
            self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, textnode):
        try:
            return self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url
        except Exception:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
