def pattern(n: int, m: int):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(j, end=" ")
        print()


pattern(5, 5)
