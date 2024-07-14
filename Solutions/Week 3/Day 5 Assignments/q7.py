my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25]

maxi = float("-inf")
n = len(my_list)
for i in range(n):
    if my_list[i] > maxi:
        maxi = my_list[i]
print(f"Maximum number = {maxi}")


"""
Also check the solution below
will be used in DSA
"""
# maxi = float("-inf")
# n = len(my_list)
# for i in range(n):
#     maxi = max(maxi, my_list[i])
# print(f"Maximum number = {maxi}")
