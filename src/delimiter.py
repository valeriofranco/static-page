from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        delimiter_count = 0
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        for character in node.text:
            if character == delimiter:
                delimiter_count += 1
            

        if delimiter_count % 2 != 0:
            raise Exception ("invalid Markdown syntax")
        
        split_node = node.text.split(delimiter)
        first_node = split_node[0]
        first_node = first_node[:-1]
        last_node = split_node[2]
        last_node = last_node[1:]
        new_nodes.append(TextNode(first_node,TextType.TEXT))
        
        if delimiter == "`":
            new_nodes.append(TextNode(split_node[1],TextType.CODE))
        elif delimiter == "**":
            new_nodes.append(TextNode(split_node[1],TextType.BOLD))
        elif delimiter == "_":
            new_nodes.append(TextNode(split_node[1],TextType.ITALIC))
        else:
            raise Exception("wrong or invalid delimiter")
        new_nodes.append(TextNode(last_node,TextType.TEXT))
        
    print(new_nodes)
    return new_nodes

        
            




node = TextNode("This is text with a `code block` word", TextType.TEXT)
split_nodes_delimiter([node], "`", TextType.CODE)