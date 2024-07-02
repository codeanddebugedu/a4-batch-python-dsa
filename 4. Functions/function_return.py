def add(n1, n2, n3):
    total = n1 + n2 + n3
    return total


def add_without_return(n1, n2, n3):
    total = n1 + n2 + n3
    print(total)


def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


x = add(10, 20, 30)
even_odd(x)
