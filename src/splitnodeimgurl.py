import re

from extract_markdown_img_url import extract_markdown_images, extract_markdown_links

from textnode import TextNode
from textnode import TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            images_tuple_list = extract_markdown_images(old_node.text)
            texts = []
            parsing_text = old_node.text
            for image in images_tuple_list:
                parsing_list = parsing_text.split(f"![{image[0]}]({image[1]})", 1)
                texts.append(parsing_list[0])
                if len(parsing_list)>1:
                    parsing_text = parsing_list[1]
            texts.append(parsing_text)
            for i in range(len(images_tuple_list)+len(texts)):
                if i % 2 == 0:
                    new_nodes.append(
                        TextNode(texts[int(i/2)], TextType.TEXT)
                    )
                else:
                    new_nodes.append(
                        TextNode(images_tuple_list[int(i/2)][0], TextType.IMAGE, images_tuple_list[int(i/2)][1])
                    )
            if new_nodes[0].text == "":
                new_nodes.pop(0)
            if new_nodes[len(new_nodes)-1].text == "":
                new_nodes.pop(len(new_nodes)-1)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            links_tuple_list = extract_markdown_links(old_node.text)
            texts = []
            parsing_text = old_node.text
            for link in links_tuple_list:
                parsing_list = parsing_text.split(f"[{link[0]}]({link[1]})", 1)
                texts.append(parsing_list[0])
                if len(parsing_list)>1:
                    parsing_text = parsing_list[1]
            texts.append(parsing_text)
            for i in range(len(links_tuple_list)+len(texts)):
                if i % 2 == 0:
                    new_nodes.append(
                        TextNode(texts[int(i/2)], TextType.TEXT)
                    )
                else:
                    new_nodes.append(
                        TextNode(links_tuple_list[int(i/2)][0], TextType.LINK, links_tuple_list[int(i/2)][1])
                    )
            if new_nodes[0].text == "":
                new_nodes.pop(0)
            if new_nodes[len(new_nodes)-1].text == "":
                new_nodes.pop(len(new_nodes)-1)
    return new_nodes