import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node =  HTMLNode("p","test text",None,{"href": "https//", "target": "_blank"})
        node2 = HTMLNode("p","test text",None,{"href": "https//", "target": "_blank"})
        self.assertEqual(node, node2)




    
if __name__ == "__main__":
    unittest.main()