"""
start end / total of all even numbers
1     100
"""

start = 1
end = 10

i = start
j = end

total = 0
while i <= j:
    if i % 2 == 0:
        total = total + i
    i += 1
print(total)
