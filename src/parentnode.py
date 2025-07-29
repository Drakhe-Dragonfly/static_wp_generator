from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag set when it is required")
        if self.children == None:
            raise ValueError("no children set when it is required")
        if len(self.children) < 1:
            raise ValueError("No children found when it is required")
        html_text = f"<{self.tag}>"
        for child in self.children:
            try:
                html_text += child.to_html()
            except Exception:
                raise ValueError("child cannot be None")
        html_text += f"</{self.tag}>"
        return html_text