import re

def extract_markdown_images(text):
    regex_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return regex_matches


def extract_markdown_links(text):
    regex_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return regex_matches