# language good a is python

my_string = "python is a good language"

words = my_string.split()
print(words)

# words.reverse()
words = words[::-1]
print(words)

ans = " ".join(word for word in words)
print(ans)
