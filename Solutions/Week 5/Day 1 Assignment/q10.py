def remove_duplicates(s: str) -> str:
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result


my_string = "aaabcccderrggffaabbcc"
print(remove_duplicates(my_string))
