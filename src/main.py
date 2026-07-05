from textnode import TextNode,TextType
from copy_static import copy_files,delete_content_destination
from generate_page import generate_page,generate_pages_recursive
import sys
def main():
    if sys.argv == "":
        basepath = "/"
    else:
        basepath = sys.argv[0]
    delete_content_destination("docs")
    copy_files("static","docs")
    generate_pages_recursive("content","template.html","docs",basepath)
    
main()
