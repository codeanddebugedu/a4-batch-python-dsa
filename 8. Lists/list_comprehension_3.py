"""
i -> 1 to 10

1 3 5 7 9 -> ODD
2 4 6 8 -> EVEN
"""

my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
# print(my_list)

my_list = [34, 67, 45, 32, 89, 80, 97, 94]

# ans = [num for num in my_list if num % 2 == 0]
ans = [my_list[i] for i in range(0, len(my_list)) if my_list[i] % 2 == 0]
print(ans)
