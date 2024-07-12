# Tell me the sum of all even numbers

my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
n = len(my_list)
total = 0

for index in range(0, n):
    if my_list[index] % 2 == 0:
        total = total + my_list[index]
print(total)

total = 0
for num in my_list:
    if num % 2 == 0:
        total = total + num
print(total)
