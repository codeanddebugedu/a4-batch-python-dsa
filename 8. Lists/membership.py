# Membership - in / not in

# my_list = [3, 6, 7, 5, 6, 6, 7, 8]

# print(6 in my_list)
# print(10 not in my_list)
my_list = [1, 4, 5, 4, 4, 4, 3, 7, 8, 9, 9, 8, 9]

result = []

for num in my_list:
    if num not in result:
        result.append(num)
    # if result.count(num) == 0:
    #     result.append(num)

print(result)
