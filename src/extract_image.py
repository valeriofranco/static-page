import re


def extract_markdown_images(text):
    new_list:list[tuple] = []
 
    both_match  = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)

    return both_match


def extract_markdown_links(text):
    new_list:list[tuple] = []

    both_match  = re.findall(r" (?<!!)\[(.*?)\]\((.*?)\)",text)

    return both_match










text = "This is text with a ![rick [roll[roll]]](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
extract_markdown_images(text)
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
extract_markdown_links(text)
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]