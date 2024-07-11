# for i in range(5, 0, -1):
#     for j in range(i, 5 + 1):
#         print(j, end=" ")
#     print()
# for i in range(2, 5 + 1):
#     for j in range(i, 5 + 1):
#         print(j, end=" ")
#     print()


n = int(input("Enter number of lines = "))
for i in range(n // 2 + 1, 0, -1):
    for j in range(i, (n // 2 + 1) + 1):
        print(j, end=" ")
    print()
for i in range(2, (n // 2 + 1) + 1):
    for j in range(i, (n // 2 + 1) + 1):
        print(j, end=" ")
    print()
