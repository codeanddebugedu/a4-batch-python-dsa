def replace(s: str) -> str:
    result = ""
    for char in s:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


my_string = "python is a very easy coding language to learn"
print(replace(my_string))
