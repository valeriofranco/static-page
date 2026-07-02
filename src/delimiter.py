from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        print(node.text_type)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            break

        #check if right amount of delimiters
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0 or delimiter not in node.text:
            raise Exception("invalid markdown syntax")

        #append list of TextNode either as text or as chosen TextType
        for i in range(0,len(split_node)):
            if split_node[i] == "" or split_node[i] == " ":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i],text_type))
    print(new_nodes)
    return new_nodes
        
            




node = TextNode("This is text with a `code block` word", TextType.BOLD)
split_nodes_delimiter([node], "`", TextType.CODE)

