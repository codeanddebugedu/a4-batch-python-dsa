# for i in range(1, 5 + 1):
#     for j in range(1, 5 - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for i in range(4, 0, -1):
#     for j in range(1, 5 - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()

n = int(input("Enter number of lines = "))
for i in range(1, (n // 2 + 1) + 1):
    for j in range(1, (n // 2 + 1) - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(1, (n // 2 + 1) - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()
