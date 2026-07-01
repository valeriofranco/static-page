class HTMLNode():
    def __init__(self, tag: str | None=None, value: str | None=None, children:list["HTMLNode"] | None=None, props:dict[str:str] | None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        message = ""
        if self.props == {} or self.props == None:
            return message
        for key in self.props:
            message += " " + key + "=" + '"' + self.props[key] + '"'
        return message
    
    def __eq__(self, other: "HTMLNode"):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
         return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self,tag: str | None, value: str, props:dict[str:str] | None=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None or self.tag == "":
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
    def __eq__(self, other: "HTMLNode"):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children:list["HTMLNode"], props:dict[str:str] | None=None):
        super().__init__(tag=tag, value = None, children=children, props=props)
    


    def to_html(self):
        if self.tag == None:
            raise ValueError("all parent nodes must have a tag")
        if self.children == None:
            raise ValueError("all parent nodes must have children nodes")
        message = ""
        for child in self.children:
            message += child.to_html()
        return f"<{self.tag}>{message}</{self.tag}>"   