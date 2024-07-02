def is_curzon(num):
    return (2**num + 1) % (2 * num + 1) == 0


n = int(input())
print(is_curzon(n))
