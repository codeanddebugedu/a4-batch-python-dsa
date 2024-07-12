# Length = 9
# 0 to 8
# 8 to 0
my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

n = len(my_list)

# Iterate by Index
# for i in range(0, n):
#     print(my_list[i])
for i in range(n - 1, -1, -1):
    print(my_list[i])
