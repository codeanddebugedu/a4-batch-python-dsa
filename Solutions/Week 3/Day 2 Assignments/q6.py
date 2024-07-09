def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(i, 6):
            print(j, end=" ")
        print()


pattern(5)
