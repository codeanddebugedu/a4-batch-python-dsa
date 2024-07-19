# Write a program to remove the nth index element from a list using a function.
from typing import List


def removeNth(lst: List, index: int) -> None:
    n = len(lst)
    if index >= n:
        print("Cannot pop, index is out of range")
        return  # To get out from function
    lst.pop(index)


my_list = [5, 6, 4, 3, 5, 7, 8, 9, 8, 7]
print(my_list)

removeNth(my_list, 0)
print(my_list)
