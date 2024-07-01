a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("equilateral")
    elif a == b or b == c or a == c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("invalid")
