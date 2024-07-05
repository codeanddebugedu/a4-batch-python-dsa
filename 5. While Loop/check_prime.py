def countfactors(num: int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count


def check_prime(n: int) -> bool:
    factors = countfactors(n)
    if factors == 2:
        return True
    return False


print(check_prime(10))
print(check_prime(11))
print(check_prime(17))
