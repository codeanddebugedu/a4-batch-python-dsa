"""
Make a function which as 5 integer parameters as a subject
Return True if pass
else False
"""


def marks(s1: int, s2: int, s3: int, s4: int, s5: int) -> bool:
    total = s1 + s2 + s3 + s4 + s5
    percentage = (total / 5) * 100
    return percentage >= 33

    # if percentage < 33:
    #     return False
    # return True


x = marks(55, 45, 33, 45, 40)
print(x)
