# Pass by reference


def printing_list(lst: list) -> None:
    lst[0] = 100


my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
printing_list(my_list)
print(my_list)
