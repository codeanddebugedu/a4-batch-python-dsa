my_list = [43, 65, 12, 89, 67, 56, 49, 86, 111]
print(f"My_list = {my_list}")
print(f"My_list ID = {id(my_list)}")


# my_list[:] = [1, 2, 3]
b = my_list[:]  # .copy()
print(f"B = {b}")
print(f"B ID = {id(b)}")
