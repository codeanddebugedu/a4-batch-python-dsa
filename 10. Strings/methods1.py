a = "14328493"

# print(a.isupper())
# print(a.islower())
# print(a.isalpha())
# print(a.isalnum())
print(a.isdigit())


num = input("Enter a number = ")
if num.isdigit():
    print(int(num) + 10)
else:
    print("Error")
