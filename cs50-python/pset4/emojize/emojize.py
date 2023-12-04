from emoji import emojize

emoji_input = input("Input: ")
print(f"Output: {emojize(emoji_input, language='alias')}")
