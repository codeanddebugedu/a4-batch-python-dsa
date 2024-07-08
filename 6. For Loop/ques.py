"""
start 5
end 26

1. start to end, total of all numbers (5+6+7+8...25+26)
2. start to end, total of all numbers divisible by 7
"""

start = int(input("Enter number = "))
end = int(input("Enter number = "))
total = 0
for i in range(start, end + 1):
    if i % 7 == 0:
        total = total + i
print(total)
