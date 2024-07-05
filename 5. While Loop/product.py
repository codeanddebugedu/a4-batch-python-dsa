"""
1 to 10, total product
1*2*3*4...*9*10
"""

# def productOfNumbers(num: int) -> int:
#     pass


def product_of_numbers(num: int) -> int:
    i = 1
    total = 1
    while i <= num:
        total = total * i
        i += 1
    return total


print(product_of_numbers(10))
