def is_prime_number(num: int) -> bool:
    # I have not used factors logic here
    # I will be explaning this in next lecture
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input("Enter n = "))
my_list = [i for i in range(2, n + 1) if is_prime_number(i)]
print(my_list)
