# for i in range(1, 6):
#     for j in range(1, 5 - i + 1):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print(6 - i, end=" ")
#     print()

n = int(input("Enter number of lines = "))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(n + 1 - i, end=" ")
    print()
