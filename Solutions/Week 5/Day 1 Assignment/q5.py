def longest_word(s: str) -> str:
    longest = ""
    current = ""
    for char in s:
        if char == " ":
            if len(current) > len(longest):
                longest = current
            current = ""
        else:
            current += char
    if len(current) > len(longest):
        longest = current
    return longest


my_string = "python is a very easy coding language to learn"
print(longest_word(my_string))
