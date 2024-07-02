def calculate_average(a: int, b: int, c: int) -> float:
    return (a + b + c) / 3


def compare_average_to_d(avg: float, d: int) -> bool:
    return avg >= d


a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Calculate the average of a, b, c
average = calculate_average(a, b, c)

# Compare the average to d
result = compare_average_to_d(average, d)

print(result)
