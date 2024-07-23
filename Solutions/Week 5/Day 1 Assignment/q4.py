def count_words(s: str) -> int:
    if not s:
        return 0
    word_count = 1
    for char in s:
        if char == " ":
            word_count += 1
    return word_count


my_string = "python is easy to learn"
print(count_words(my_string))
