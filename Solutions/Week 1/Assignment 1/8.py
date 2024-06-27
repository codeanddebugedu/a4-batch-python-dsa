"""
Ask a number from user. Print if the number is ODD or EVEN.
"""

number = int(input("Enter a number = "))
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")
