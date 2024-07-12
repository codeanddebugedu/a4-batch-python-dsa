def number_of_factors(num: int) -> int:
    i = 1
    factors = 0
    while i <= num:
        if num % i == 0:
            factors += 1
        i += 1
    return factors


def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False

    no_of_factors = number_of_factors(n)
    if no_of_factors > 2:
        return False
    return True


print(is_prime(29))
print(is_prime(15))
