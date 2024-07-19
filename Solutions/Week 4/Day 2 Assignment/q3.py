# Ask 10 numbers from the user and put them into the list.
# Now remove all the even numbers from that list

my_list = []
l = int(input("Enter length of the list = "))
for i in range(l):
    num = int(input(f"Enter element {i+1} = "))
    my_list.append(num)

result = []
for num in my_list:
    if num % 2 != 0:
        result.append(num)

print(result)


# Alternate way
# for i in range(l):
#     if my_list[i]%2!=0:
#         result.append(my_list[i])
