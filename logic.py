def translate_to_hacker(text: str) -> str:
    replacements = {
        "a": "4",
        "o": "0",
        "i": "1",
        "e": "3",
        "а": "4",
        "о": "0",
        "и": "1",
        "е": "3"
    }


    hacker_text = ""
    for char in text.lower():
        if char in replacements:
            hacker_text += replacements[char]
        else:
            hacker_text += char
    return hacker_text