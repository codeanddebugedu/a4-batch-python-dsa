def factorial(n: int) -> int:
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


print(factorial(12))
