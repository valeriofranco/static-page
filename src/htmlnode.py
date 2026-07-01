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
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("all leaf nodes must have a value")
