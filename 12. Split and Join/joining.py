# SPlit -> String to List
# Joining -> List to String


# a n i r u d h
my_list = ["a", "n", "i", "r", "u", "d", "h"]


# result = "".join(ch for ch in my_list)
result = "-".join(ch + "5" for ch in my_list)
print(result)
# my_list = ["a", 4, 5, 6, 7, 8, 7, "Anirudh", "x", "y", "z"]

# print("".join(str(ch) for ch in my_list))
