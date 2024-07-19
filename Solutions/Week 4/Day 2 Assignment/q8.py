# Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []

for num in my_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


print(f"even = {even}")
print(f"odd = {odd}")
