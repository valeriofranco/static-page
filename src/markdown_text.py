


def markdown_to_blocks(markdown):
    result = []
    lines = markdown.split("\n\n")
    
    for line in lines:
        if line.strip() == "":
            continue
        result.append(line.strip())

    return result






