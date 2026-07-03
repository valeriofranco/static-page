from split import split_nodes_link,split_nodes_image
from delimiter import split_nodes_delimiter
from textnode import TextNode,TextType
def text_to_textnodes(text):
    textnode = TextNode(text,TextType.TEXT)
    bolded_text = split_nodes_delimiter([textnode],"**",TextType.BOLD)
    italic_text = split_nodes_delimiter(bolded_text,"_",TextType.ITALIC)
    coded_text = split_nodes_delimiter(italic_text,"`",TextType.CODE)
    linked_text = split_nodes_link(coded_text)
    imaged_text = split_nodes_image(linked_text)
    return imaged_text


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

print(text_to_textnodes(text))
