from copy import deepcopy

a = [1, 2, 3, [100, 200, 300], 7, 9]

# b = a.copy()  # Shallow Copy
b = deepcopy(a)

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print(f"a = {a}")
print(f"b = {b}")

b[0] = 100
b[3][0] = 1
print(f"a = {a}")
print(f"b = {b}")
