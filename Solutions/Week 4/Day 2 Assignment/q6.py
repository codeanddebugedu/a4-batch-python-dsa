# Make two lists of same length and pass it to a function.
# Return a third list where each element is the sum of index
from typing import List


def additionOfList(lst1: List[int], lst2: List[int]) -> List[int]:
    n = len(lst1)
    result = []
    for i in range(n):
        total = lst1[i] + lst2[i]
        result.append(total)
    return result


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 4, 3, 1]

ans = additionOfList(list1, list2)
print(ans)
