string = input()
listed = string.split()
modified_listed = []
for word in listed:
    modified_listed.append("🙂" if word == ":)" else "🙁" if word == ":(" else word)
print(" ".join(modified_listed))
