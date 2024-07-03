"""
5674
10983


1. How many numbers are divisible by 7?             -> 759
2. How many numbers are divisible by both 2 and 7?  -> 379
"""

i = 5674
j = 10983
count = 0
while i <= j:
    if i % 7 == 0:
        count = count + 1
    i += 1
print(count)
