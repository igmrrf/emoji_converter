import re


def replace_with_emoji(tweet):
    emojis = {
        ":wink": "😉",
        ":love": "💕",
        ":cool": "😎",
        ":inlove": "😍",
        ":angry": "😠",
        ":developer": "👨‍💻",
        ":developress": "👩‍💻"
    }

    def repl(m):
        return m.group(1) + emojis.get(m.group(2), m.group(2))

    return re.sub(r"(^|\s)([:]\w+)\b", repl, tweet)


message = input("> ")
print(replace_with_emoji(message))


# def replace_with_emoji(tweet):
#     texts = tweet.split(" ")
#     emojis = {
#         ":wink": "😉",
#         ":love": "💕",
#         ":cool": "😎",
#         ":inlove": "😍",
#         ":angry": "😠",
#         ":developer": "👨‍💻",
#         ":developress": "👩‍💻"
#     }

#     replaced = ""
#     for text in texts:
#         replaced += emojis.get(text, text) + " "
#     return replaced


# message = input("> ")
# print(replace_with_emoji(message))
