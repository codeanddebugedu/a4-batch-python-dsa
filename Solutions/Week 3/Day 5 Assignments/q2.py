my_list = [4, 8, 6, 5, 3, 12, 1, 3, 6]

# Method 1
# n = len(my_list)
# odd_count = 0
# even_count = 0
# for i in range(n):
#     if my_list[i] % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Total even numbers = {even_count}")
# print(f"Total odd numbers = {odd_count}")

# Method 2
odd_count = 0
even_count = 0
for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total even numbers = {even_count}")
print(f"Total odd numbers = {odd_count}")
