"""
Ask a number from user.

num is divisible by 3 -> FOO
num is divisible by 5 -> BAR

num is divisible by 3 and 5 -> FOOBAR

else
-> Invalid
"""

num = int(input("Enter number = "))  # 15
if num % 3 == 0 and num % 5 == 0:
    print("FooBar")
elif num % 3 == 0:
    print("Foo")
elif num % 5 == 0:
    print("Bar")
else:
    print("Invalid")
