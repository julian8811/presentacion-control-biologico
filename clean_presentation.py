import re
import sys

def remove_emojis(text):
    # This regex matches most emojis
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f700-\U0001f77f"  # alchemical symbols
        "\U0001f780-\U0001f7ff"  # Geometric Shapes Extended
        "\U0001f800-\U0001f8ff"  # Supplemental Arrows-C
        "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
        "\U0001fa00-\U0001fa6f"  # Chess Symbols
        "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
        "\u2600-\u26ff"          # misc symbols
        "\u2700-\u27bf"          # dingbats
        "\u2300-\u23ff"          # misc technical
        "\u2b50"                 # star
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def main():
    file_path = '/home/julian/diapos_control/Presentacion_Control_Biologico.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove emojis
    content = remove_emojis(content)

    # Replace " - " or " — " with ", " (avoiding HTML comments)
    # We will do this carefully using regex:
    # Match " - " or " — " or " —" or " -" that is NOT inside HTML tags if possible.
    # A simpler way is just to replace " - " with ", " and " — " with ", "
    # Also "—" (without spaces) if it's used as a separator. Let's just do the ones with spaces first.
    content = content.replace(" — ", ", ")
    content = content.replace(" —", ",")
    content = content.replace("— ", ", ")
    content = content.replace("—", ",")
    
    # " - " is a bit risky because of CSS values like "calc(100% - 20px)" or "margin: 10px - 5px" 
    # Let's use a regex that only replaces " - " if it's followed by a letter, and not inside a style tag.
    # Alternatively, just let me check how many " - " there are in the text.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
