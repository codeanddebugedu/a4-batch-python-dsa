num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"{largest} {smallest}")
