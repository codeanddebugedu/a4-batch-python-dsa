def sumDivisibleBy3And6(a: int, b: int) -> int:
    if a > b:
        a, b = b, a  # Ensure a is less than or equal to b
    total_sum = 0
    current = a
    while current <= b:
        if current % 3 == 0 and current % 6 == 0:
            total_sum += current
        current += 1
    return total_sum


print(sumDivisibleBy3And6(0, 0))
