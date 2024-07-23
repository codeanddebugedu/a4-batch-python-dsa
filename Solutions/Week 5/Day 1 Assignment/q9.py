def count_digits(s: str) -> int:
    digit_count = 0
    for char in s:
        if "0" <= char <= "9":
            digit_count += 1
    return digit_count


my_string = "abcd1239"
print(count_digits(my_string))
