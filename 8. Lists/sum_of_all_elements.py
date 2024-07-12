my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

total = 0
n = len(my_list)
for i in range(0, n):
    total = total + my_list[i]
print(total)

total2 = 0
for i in my_list:
    total2 = total2 + i
print(total2)
