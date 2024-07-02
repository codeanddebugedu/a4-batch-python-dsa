def product(n1, n2):
    ans = n1 * n2
    return ans


def check_div_by_5(num):
    if num % 5 == 0:
        print("Yes")
    else:
        print("No")


x = product(10, 15)
print(x)

# ----
y = product(11, 22)
print(y)
check_div_by_5(y)
