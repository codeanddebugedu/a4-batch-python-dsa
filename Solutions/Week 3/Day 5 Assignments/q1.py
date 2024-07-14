my_list = [4, 8, 6, 5, 3, 12, 1, 3]

# Method 1
# n = len(my_list)
# count = 0
# for i in range(n):
#     if my_list[i] % 2 == 1:
#         count += 1
# print(f"Total odd numbers = {count}")

# Method 2
count = 0
for num in my_list:
    if num % 2 == 1:
        count += 1
print(f"Total odd numbers = {count}")
