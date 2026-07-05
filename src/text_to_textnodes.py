from split import split_nodes_link,split_nodes_image
from delimiter import split_nodes_delimiter
from textnode import TextNode,TextType
def text_to_textnodes(text):
    textnode = [TextNode(text,TextType.TEXT)]
    bolded_text = split_nodes_delimiter(textnode,"**",TextType.BOLD)
    italic_text = split_nodes_delimiter(bolded_text,"_",TextType.ITALIC)
    coded_text = split_nodes_delimiter(italic_text,"`",TextType.CODE)
    imaged_text = split_nodes_image(coded_text)
    linked_text = split_nodes_link(imaged_text)
    return linked_text




