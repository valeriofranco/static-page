from textnode import TextType,TextNode
from extract_image import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            pass
        print(node.text)
        image_text = extract_markdown_images(node.text)
        print(image_text)
        print(image_text[0][0])
        print(image_text[0][1])
        print(image_text[1][0])
        print(image_text[1][1])
        split1 = node.text.split(f"![{image_text[0][0]}]({image_text[0][1]})")
        split1 = split1[1]
        print(split1.split(f"![{image_text[1][0]}]({image_text[1][1]})"))
        middle_text = node.text.split(f"({image_text[0][1]})")
        new_nodes.append()
        #node.text.split(extract_markdown_images(node.text)[0])
    return new_nodes
        


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass







node = TextNode(
    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]