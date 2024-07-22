"""
Keep on asking characters from the user.

Stop it unitil he/she presses q


Enter char = r
Enter char = 1
Enter char = p
Enter char = l
Enter char = q
"""


def askchars() -> str:
    my_string = ""
    while True:
        char = input("Enter a char = ")
        if char == "q" or char == "Q":
            break
        my_string += char

    return my_string
