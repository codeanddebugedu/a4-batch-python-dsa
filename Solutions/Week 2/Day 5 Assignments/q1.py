def number_of_factors(num: int) -> int:
    i = 1
    factors = 0
    while i <= num:
        if num % i == 0:
            factors += 1
        i += 1
    return factors


print(number_of_factors(100))
