import re


def extract_markdown_images(text):
    new_list:list[tuple] = []
 
    both_match  = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)

    return both_match


def extract_markdown_links(text):
    new_list:list[tuple] = []

    both_match  = re.findall(r" (?<!!)\[(.*?)\]\((.*?)\)",text)

    return both_match










