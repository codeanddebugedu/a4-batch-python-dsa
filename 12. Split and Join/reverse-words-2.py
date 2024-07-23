my_string = "python is a good language"

# Output 👇
# egaugnal doog a si nohtyp

words = my_string.split()
# words.reverse()
print(" ".join(word[::-1] for word in words[::-1]))
