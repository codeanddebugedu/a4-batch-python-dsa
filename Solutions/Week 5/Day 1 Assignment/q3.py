def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for char in s:
        if char not in vowels:
            no_vowels += char
    return no_vowels


my_string = "abcdefghij"
print(remove_vowels(my_string))
