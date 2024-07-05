def print_factors(num: int) -> None:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1


def print_factors_2(num: int) -> None:
    i = 1
    while i <= num // 2:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print(num)


print_factors_2(200000000)
