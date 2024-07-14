my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25]

mini = float("inf")
n = len(my_list)
for i in range(n):
    if my_list[i] < mini:
        mini = my_list[i]
print(f"Minimum number = {mini}")


"""
Also check the solution below
will be used in DSA
"""
# mini = float("inf")
# n = len(my_list)
# for i in range(n):
#     mini = min(mini, my_list[i])
# print(f"Minimum number = {mini}")
