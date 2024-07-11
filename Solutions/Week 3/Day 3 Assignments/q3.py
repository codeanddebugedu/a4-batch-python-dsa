# for i in range(5, 0, -1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(5, i - 1, -1):
#         print(k, end=" ")
#     print()

n = int(input("Enter number of lines = "))
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(n, i - 1, -1):
        print(k, end=" ")
    print()
