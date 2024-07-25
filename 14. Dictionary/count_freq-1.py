my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]

"""
{
    
}
"""
my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
