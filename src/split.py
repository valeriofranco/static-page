from textnode import TextType,TextNode
from extract_image import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            pass

        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
            continue
        image_text = extract_markdown_images(node.text)
        
        new_node = []
        remaining_text = node.text
        for i in range (0, len(image_text)):
            temp_list = remaining_text.split(f"![{image_text[i][0]}]({image_text[i][1]})",1)
            if len(temp_list) > 1:
                remaining_text = temp_list[1]
            if temp_list[0] == "":
                continue
            
            new_node.append(temp_list[0])
            new_node.append((image_text[i][0],image_text[i][1]))
            
        if temp_list[1] != "":
            new_node.append(temp_list[1])

        for i in range(0,len(new_node)):
            if not isinstance(new_node[i],tuple):     
                new_nodes.append(TextNode(new_node[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(new_node[i][0],TextType.IMAGE,new_node[i][1]))

    return new_nodes
        

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
            continue
        link_text = extract_markdown_links(node.text)
        
        new_node = []
        remaining_text = node.text
        for i in range (0, len(link_text)):
            temp_list = remaining_text.split(f"[{link_text[i][0]}]({link_text[i][1]})",1)
            if len(temp_list) > 1:
                remaining_text = temp_list[1]
            if temp_list[0] != "":
                new_node.append(temp_list[0])
            new_node.append((link_text[i][0], link_text[i][1]))
            
        if temp_list[1] != "":
            new_node.append(temp_list[1])

        for i in range(0,len(new_node)):
            if not isinstance(new_node[i],tuple):     
                new_nodes.append(TextNode(new_node[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(new_node[i][0],TextType.LINK,new_node[i][1]))

    return new_nodes
