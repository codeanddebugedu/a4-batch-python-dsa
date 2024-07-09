def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(5, i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)
