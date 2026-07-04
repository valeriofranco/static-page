from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    


def block_to_block_type(text_block):
    print(text_block)
    text_lines = text_block.split("\n")
    new_lines = []
    for line in text_lines:
        if line == "" or line == " ":
            continue
        new_lines.append(line)
    if new_lines[0].startswith(("# ","## ","### ","#### ","##### ","###### ")) and len(new_lines) == 1:
        return BlockType.HEADING
    elif new_lines[0].startswith("```") and new_lines[-1].endswith("```"):
        return BlockType.CODE


    for line in new_lines:
        if not line.startswith(">"):
            result = BlockType.PARAGRAPH
            break
        result = BlockType.QUOTE
    if result != BlockType.PARAGRAPH:
        return result



    for line in new_lines:
        if not line.startswith("- "):
            result = BlockType.PARAGRAPH
            break
        result = BlockType.UNORDERED_LIST
    if result != BlockType.PARAGRAPH:
        return result


    for i in range (0, len(new_lines)):
        if not new_lines[i].startswith(f"{i+1}. "):
            result = BlockType.PARAGRAPH
            break
        result = BlockType.ORDERED_LIST
    if result != BlockType.PARAGRAPH:
        return result

    return result
        
