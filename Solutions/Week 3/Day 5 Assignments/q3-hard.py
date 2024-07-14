my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
for num in my_list:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
