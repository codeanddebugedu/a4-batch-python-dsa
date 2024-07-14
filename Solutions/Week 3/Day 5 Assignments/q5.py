my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]

total_sum = 0
total_product = 1

n = len(my_list)
for i in range(n):
    total_sum += my_list[i]
    total_product *= my_list[i]

# for num in my_list:
#     total_sum += num
#     total_product *= num


print(f"Total sum = {total_sum}")
print(f"Total product = {total_product}")
