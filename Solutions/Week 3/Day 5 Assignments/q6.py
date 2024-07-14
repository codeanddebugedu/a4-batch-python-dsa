my_list = [5, 8, 10, 15, 2, 4, 95, 34, 25]

n = len(my_list)
for i in range(n - 1, -1, -1):
    if my_list[i] % 5 == 0:
        print(my_list[i], end=" ")
