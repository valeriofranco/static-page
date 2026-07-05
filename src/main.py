from textnode import TextNode,TextType
from copy_static import copy_files,delete_content_destination
from generate_page import generate_page,generate_pages_recursive
def main():
    delete_content_destination("public")
    copy_files("static","public")
    generate_pages_recursive("content","template.html","public")
main()