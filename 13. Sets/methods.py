set1 = {76, 43, 19, 83, 41, 33, 33, 33, 33}
print(set1)

set1.add(100)
print(set1)

set1.remove(43)
print(set1)

another_set = set1.copy()
another_set.add(1000)

print(set1)
print(another_set)
# set1.clear()
# print(set1)
