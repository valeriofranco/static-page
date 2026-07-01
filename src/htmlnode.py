class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
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
            message += " " + key + self.props[key]

    def __repr__(self):
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)