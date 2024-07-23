def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


def reverse_string2(s):
    return s[::-1]


my_string = "abcdefg"
print(reverse_string(my_string))
print(reverse_string2(my_string))
