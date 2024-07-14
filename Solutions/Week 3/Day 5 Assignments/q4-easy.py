def is_prime_number(num: int) -> bool:
    # I have not used factors logic here
    # I will be explaning this in next lecture
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
total = 0
for num in my_list:
    if is_prime_number(num):
        total += num
print(f"Total of all prime numbers = {total}")
