def is_prime_number(num: int) -> bool:
    # I have not used factors logic here
    # I will be explaning this in next lecture
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [4, 8, 6, 19, 3, 12, 1, 7, 6, 2]
max_prime_number = 0
for num in my_list:
    if is_prime_number(num):
        if num > max_prime_number:
            max_prime_number = num

if max_prime_number != 0:
    print(f"Largest prime number = {max_prime_number}")
else:
    print("No prime numbers present in the list")
