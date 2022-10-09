def func_emoji(message):
    words = message.split(" ")
    emoji_map = {
        ":)": "🙂",
        ":(": "😞",
        "xD": "😆",
        "rofl": "🤣"
    }
    output = ""
    for word in words:
        output += emoji_map.get(word, word) + " "
    return output


message = input("> ")
print(func_emoji(message))
