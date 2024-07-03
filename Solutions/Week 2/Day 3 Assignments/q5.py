def squares_sum(n):
    i = 1
    sum = 0
    while n >= i:
        x = i**2
        sum += x
        i = i + 1
    return sum


print(squares_sum(23))
