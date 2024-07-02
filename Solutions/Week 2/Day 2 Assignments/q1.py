def find_largest(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = int(input())
b = int(input())
c = int(input())

largest = find_largest(a, b, c)

print(largest)
