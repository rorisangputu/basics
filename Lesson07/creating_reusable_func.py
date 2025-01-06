##Emoji converter



def emoji_converter(sentence):
    emojis = {
        ":)": "😃",
        ":p": "😋",
        ":(": "😞"
    }

    words = sentence.split(' ')
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
sentence_with_emoji = emoji_converter(message)
print(sentence_with_emoji)