import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode
from textnode import TextNode,text_node_to_html_node,TextType


class TestHTMLNode(unittest.TestCase):
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



    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    
if __name__ == "__main__":
    unittest.main()