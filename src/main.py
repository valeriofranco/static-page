from textnode import TextNode,TextType
from copy_static import copy_files,delete_content_destination
from generate_page import generate_page
def main():
    delete_content_destination("public")
    copy_files("static","public")
    generate_page("content/index.md","template.html","public/index.html")
main()