def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(i, 6):
            print(j, end=" ")
        print()


pattern(5)
