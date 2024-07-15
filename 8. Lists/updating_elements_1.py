my_list = [4, 5, 3, 1, 7, 6, 5, 9, 100]

# By index

n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 1
    else:
        my_list[i] = my_list[i] - 1

print(my_list)
