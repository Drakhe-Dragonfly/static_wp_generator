from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            html_text = f"<{self.tag}"
            for prop in self.props :
                html_text += f' {prop}="{self.props[prop]}"'
            html_text += f'>{self.value}</{self.tag}>'
            return html_text
            # return f'<{self.tag} href="{self.props["href"]}">{self.value}</{self.tag}>'