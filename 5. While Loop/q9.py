# 1 to 10, even number, count how many are there?

count = 0
i = 1

while i <= 10:
    if i % 2 == 0:
        count += 1
    i += 1

print(count)
