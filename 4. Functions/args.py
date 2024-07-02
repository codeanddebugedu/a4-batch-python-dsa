# Spread,Splat


def add(n1, n2, *args):
    print(f"n1 -> {n1}")
    print(f"n2 -> {n2}")
    print(f"n3 -> {args}")


add(10, 20, 30, "ANirudh", True, 55.55)
# add(10, 20, 6, 77, 55)


# *args
def add_2(*args):
    print(f"num -> {args}")


# add(10, 20, 30, 40)
# add(10, 20)
# add_2(10, 20, 54, 5654, 7654, 7, 657, 657, 65765)
