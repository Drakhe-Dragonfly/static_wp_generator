from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if delimiter in ["", " ", None]:
        raise Exception("incorrect delimiter, it has a 1/2 chance to make an error")
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            new_text_list = old_node.text.split(delimiter)
            if len(new_text_list) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for i in range(0, len(new_text_list)):
                if i % 2 == 1:
                    new_nodes.append(TextNode(new_text_list[i], text_type))
                else:
                    new_nodes.append(TextNode(new_text_list[i], TextType.TEXT))
    if new_nodes[0].text == "":
        new_nodes.pop(0)
    if new_nodes[len(new_nodes)-1].text == "":
        new_nodes.pop(len(new_nodes)-1)
    # print(new_nodes)
    return new_nodes