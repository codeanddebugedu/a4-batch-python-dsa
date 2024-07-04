def pattern(n: int) -> None:
    num = 1
    i = 1
    while i <= n:
        print(num)
        num = (num * 10) + 1
        i += 1


pattern(5)
