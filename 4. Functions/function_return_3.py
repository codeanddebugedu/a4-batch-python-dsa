# With parameters and with return


def average(n1: int, n2: int, n3: int, n4: int) -> float:
    total = n1 + n2 + n3 + n4
    return total / 4


def add(num1: int, num2: int) -> None:
    total = num1 + num2
    print(total)


def concat(first_name: str, last_name: str) -> str:
    return first_name + last_name


#
ans = concat("abc", "xyz")
print(ans)
# x = average(10, 20, 43, 22)
# print(x)

# add(10, 20)
