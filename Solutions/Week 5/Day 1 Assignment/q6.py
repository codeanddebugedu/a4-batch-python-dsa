def capitalize(s: str) -> str:
    result = ""
    is_new_word = True
    for char in s:
        if is_new_word and "a" <= char <= "z":
            result += chr(ord(char) - 32)
            is_new_word = False
        else:
            result += char
        if char == " ":
            is_new_word = True
    return result


my_string = "python is a very easy coding language to learn"
print(capitalize(my_string))
