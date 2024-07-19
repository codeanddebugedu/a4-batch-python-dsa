# Write a Python Program to find sum and average of List in Python

my_list = [4, 5, 6, 1, 3, 6, 7, 4, 3]
n = len(my_list)

total = 0
for i in range(n):
    total = total + my_list[i]

print(f"Total = {total}")
print(f"Average = {total/n}")
