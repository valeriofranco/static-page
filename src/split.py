from textnode import TextType,TextNode
from extract_image import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            pass
        #print(node.text)
        if extract_markdown_images(node.text) == []:
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
            pass

        if extract_markdown_links(node.text) == []:
            continue
        link_text = extract_markdown_links(node.text)
        
        new_node = []
        remaining_text = node.text
        for i in range (0, len(link_text)):
            temp_list = remaining_text.split(f"[{link_text[i][0]}]({link_text[i][1]})",1)
            if len(temp_list) > 1:
                remaining_text = temp_list[1]
            if temp_list[0] == "":
                continue
            
            new_node.append(temp_list[0])
            new_node.append((link_text[i][0],link_text[i][1]))

        for i in range(0,len(new_node)):
            if not isinstance(new_node[i],tuple):     
                new_nodes.append(TextNode(new_node[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(new_node[i][0],TextType.LINK,new_node[i][1]))

    return new_nodes





"""link_node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([link_node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

image_node = TextNode(
    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([image_node])"""