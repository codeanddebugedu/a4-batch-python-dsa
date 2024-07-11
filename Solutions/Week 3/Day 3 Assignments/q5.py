# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(i, 6):
#         print(i, end=" ")
#     print()

n = int(input("Enter number of lines = "))
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, n + 1):
        print(i, end=" ")
    print()
