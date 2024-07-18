# my_list = [i for i in range(1, 101) if i % 2 == 0]
# print(my_list)


def is_prime_number(num: int) -> bool:
    # I have not used factors logic here
    # I will be explaning this in next lecture
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [i for i in range(1, 101) if is_prime_number(i)]
print(my_list)
