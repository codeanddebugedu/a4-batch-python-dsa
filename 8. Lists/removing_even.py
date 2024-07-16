# Remove even numbers

my_list = [5, 7, 4, 8, 10, 12, 14]
result = []
print(my_list)

n = len(my_list)

for num in my_list:
    if num % 2 == 0:
        my_list.remove(num)
print(my_list)
# for i in range(0, n):
#     if my_list[i] % 2 != 0:
#         result.append(my_list[i])

# print(my_list)
# print(result)
