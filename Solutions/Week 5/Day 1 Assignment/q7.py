def replace(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if ("a" <= char <= "z" or "A" <= char <= "Z") and char not in vowels:
            result += "*"
        else:
            result += char
    return result


my_string = "python is a very easy coding language to learn"
print(replace(my_string))
