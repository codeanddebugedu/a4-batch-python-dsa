a = 5
b = 10

print(a > 5 and b >= 10)  # Output: False
print(a >= 5 or not b > 10)  # Output: True
print(not (a > 5 and b > 5))  # Output: True
print(not (a < 10 or not b < 10))  # Output: False
print(not (not a <= 5 or not b >= 10))  # Output: True
