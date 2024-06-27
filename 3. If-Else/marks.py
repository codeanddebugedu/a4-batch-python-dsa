"""
Ask a mark from a user.

91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
1 - 60 -> Fail
"""

num = int(input("Enter marks = "))  # 95
if num >= 91 and num <= 100:
    print("A")
elif num >= 81 and num <= 90:
    print("B")
elif num >= 71 and num <= 80:
    print("C")
elif num >= 61 and num <= 70:
    print("D")
elif num >= 0 and num <= 60:
    print("fail")
else:
    print("Invalid")

# if-else

# ----
