my_string = "python is a good language"

# nohtyp si a doog egaugnal

words = my_string.split()
print(words)

print("-".join(word[::-1] for word in words))
result = ""
for word in words:
    result = result + word[::-1]
    result += "-"

print(result)
print(result[:-1])
