def sumRange(a: int, b: int) -> int:
    if a > b:
        # I have not explained this yet, although you can use chatgpt, you will get it
        a, b = b, a  # Ensure a is less than or equal to b

    total = 0
    i = a
    while i <= b:
        total += i
        i += 1
    return total


print(sumRange(1, 10))
