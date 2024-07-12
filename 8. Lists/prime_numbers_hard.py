# Print all prime numbers (hard)
my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num, end=" ")
