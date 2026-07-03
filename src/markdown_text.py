


def markdown_to_blocks(markdown):
    result = []
    lines = markdown.split("\n\n")
    
    for line in lines:
        if line.strip() == "":
            continue
        result.append(line.strip())

    return result




md = """
This is **bolded** paragraph                     

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line                  

- This is a list
- with items                  
"""

