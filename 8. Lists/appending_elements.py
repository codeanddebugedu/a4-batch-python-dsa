"""
Ask a number from user = 6

Enter element = 3
Enter element = 4
Enter element = 7
Enter element = 1
Enter element = 3
Enter element = 5

[3,4,7,1,3,5]
"""

from typing import List


def create_list(length: int) -> List[int]:
    my_list = []
    for i in range(length):
        x = int(input(f"Enter element {i+1} = "))
        my_list.append(x)
    return my_list


lst = create_list(6)
print(lst)
