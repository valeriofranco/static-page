from textnode import TextNode,TextType
from copy_static import copy_files,delete_content_destination
def main():
    delete_content_destination("public")
    copy_files("static","public")
main()