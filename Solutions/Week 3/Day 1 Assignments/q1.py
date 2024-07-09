def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, 6):
            print(1, end=" ")
        print()


# Alternate Way
def pattern_2(n: int):
    for _ in range(n):
        for _ in range(5):
            print(1, end=" ")
        print()


# pattern(5)
pattern_2(3)
