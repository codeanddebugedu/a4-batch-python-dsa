# Take 10 integer inputs from user and store them in a list.
# Now, copy all the elements in another list but in reverse order.

my_list = []
l = int(input("Enter length of the list = "))
for i in range(l):
    num = int(input(f"Enter element {i+1} = "))
    my_list.append(num)

result = []
for i in range(l - 1, -1, -1):
    result.append(my_list[i])

print(f"my_list = {my_list}")
print(f"result = {result}")
