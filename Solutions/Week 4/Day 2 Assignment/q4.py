# Write a python program which prints all the values whose count is greater than 3.
# (Make sure to make a list with at least 15 numbers)


my_list = [3, 8, 7, 3, 5, 5, 5, 5, 3, 8, 3, 3, 3, 1, 3, 8, 9, 6, 7, 8, 9]
result = []


for num in my_list:
    if my_list.count(num) > 3:
        if num not in result:
            result.append(num)

print(result)
