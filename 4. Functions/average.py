# Function named average
# 3 num from user -> calculate average
def avg():
    n1 = int(input("Enter num1 = "))
    n2 = int(input("Enter num2 = "))
    n3 = int(input("Enter num3 = "))

    total = (n1 + n2 + n3) / 3

    print(f"Avg = {total}")


avg()
