import os
from markdown_to_html import markdown_to_html_node, extract_title
from htmlnode import HTMLNode,LeafNode,ParentNode
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}\n")

    with open(from_path,"r") as file:
        content_from = file.read()
    with open(template_path,"r") as other_file:
        content_template = other_file.read()
    html_node = markdown_to_html_node(content_from)
    html_str = html_node.to_html()
    title = extract_title(content_from)

    template_content_replaced = content_template.replace("{{ Content }}",html_str)
    template_fully_replaced = template_content_replaced.replace("{{ Title }}",title)

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template_fully_replaced)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files_in_dir = os.listdir(dir_path_content)
    for file in files_in_dir:
        new_path = os.path.join(dir_path_content,file)
        new_dest = os.path.join(dest_dir_path,file)
        if os.path.isfile(new_path):
            final_dest = Path(new_dest).with_suffix(".html")
            generate_page(new_path, template_path, final_dest)
        else:
            generate_pages_recursive(new_path,template_path,new_dest)
    



generate_pages_recursive("content", "template.html", "public")