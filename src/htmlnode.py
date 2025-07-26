class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string
        self.value = value # string OR None (if None then children should have a set value)
        self.children = children # list of node(s) OR None (if None then value should have a set value)
        self.props = props # dictionnary containing the properties with the name of the property and the associated value 
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            html_props = ""
            for prop in self.props:
                html_props += f" {prop}={self.props[prop]}"
            return html_props
    
    def __eq__(self, htmlnode):
        return (self.tag == htmlnode.tag) and (self.value == htmlnode.value) and (self.children == htmlnode.children) and (self.props == htmlnode.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"