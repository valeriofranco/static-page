from textnode import TextNode,TextType

def main():
    first = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(first)
main()