import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,text_node_to_html_node,TextType
from delimiter import split_nodes_delimiter
from extract_image import extract_markdown_images,extract_markdown_links
from split import split_nodes_link,split_nodes_image


class TestHTMLNode(unittest.TestCase):
    #htmlnodes test
    def test_eq(self):
        node =  HTMLNode("2","w",None,{"key":"value"})
        self.assertEqual(node.props_to_html(),' key="value"' )

    def test_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(),"" )

    def test_equal(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node,node2)

    #Leafnodes.to_html tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
        node = LeafNode("a", "Hello, world!",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')


    def test_equal_leaf(self):
        node = LeafNode("a", "Hello, world!")
        node2 = LeafNode("a", "Hello, world!")
        self.assertEqual(node,node2)

    def test_leaf_to_html_p3(self):
        node = LeafNode(None, "Hello, world!",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Hello, world!")


    #Parentnode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    
    #text_node to html_node tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text1(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text2(self):
        node = TextNode("This is a link node", TextType.LINK, "https://")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": node.url})

    def test_text3(self):
        node = TextNode("This is a image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": node.url, "alt": node.text})

    #split nodes delimiter tests
    def test_delimiter1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split_node, [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode( " word", TextType.TEXT, None)])


    def test_delimiter2(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block", TextType.BOLD, None), TextNode( " word", TextType.TEXT, None)])

    def test_delimiter3(self):
        node = TextNode("**This** is text with a **code block** word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This", TextType.BOLD, None), TextNode(" is text with a ", TextType.TEXT, None), TextNode("code block", TextType.BOLD, None), TextNode( " word", TextType.TEXT, None)])

    def test_delimiter4(self):
        node = TextNode("**This** **is** **text** **with** **a** **code** **block** **word**", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This", TextType.BOLD, None), TextNode("is", TextType.BOLD, None), TextNode("text", TextType.BOLD, None), TextNode("with", TextType.BOLD, None), 
                                      TextNode("a", TextType.BOLD, None), TextNode("code", TextType.BOLD, None), TextNode("block", TextType.BOLD, None), TextNode("word", TextType.BOLD, None)])
    
    def test_delimiter5(self):
        node = TextNode("This is text with a **code** block word", TextType.BOLD)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This is text with a **code** block word", TextType.BOLD)])

    def test_delimiter_exception(self):
        node = TextNode("This is text with a `code block** word", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(context.exception), "invalid markdown syntax")

    def test_delimiter_exception1(self):
        node = TextNode("This is text with a `code block** word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "_", TextType.CODE)

        self.assertEqual(split_node, [TextNode("This is text with a `code block** word", TextType.TEXT)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images1(self):
        matches = extract_markdown_images(
        "This is text with an ![image[image]](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image[image]", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
        "This is text with an ![image[image]](https://i.imgur.com/(zjjcJKZ.png)"
        )
        self.assertListEqual([("image[image]", "https://i.imgur.com/(zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links1(self):
        matches = extract_markdown_links(
        "This is text with an [image[image]](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image[image]", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links2(self):
        matches = extract_markdown_links(
        "This is text with an [image[image]](https://i.imgur.com/(zjjcJKZ.png)"
        )
        self.assertListEqual([("image[image]", "https://i.imgur.com/(zjjcJKZ.png")], matches)


    #split image tests
    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
        )
    
    def test_split_images1(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            
        ],
        new_nodes,
        )
    
    def test_split_images2(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
       
            
        ],
        new_nodes,
        )


    def test_split_images3(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node,node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            
        ],
        new_nodes,
        )

    #split links tests
    def test_split_links(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
        )
    
    def test_split_links1(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            
        ],
        new_nodes,
        )
    
    def test_split_links2(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
       
            
        ],
        new_nodes,
        )

    def test_split_links3(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node,node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            
        ],
        new_nodes,
        )
    

    
if __name__ == "__main__":
    unittest.main()