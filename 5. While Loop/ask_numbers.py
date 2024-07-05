"""
Keep asking a number from user until he enters zero (0)
Calculate total
"""

total = 0
while True:
    num = int(input("Enter number = "))
    if num == 0:
        break
    total = total + num
print(total)
