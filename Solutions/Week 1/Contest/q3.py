num1 = int(input())
num2 = int(input())
operation = input()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "invalid"
else:
    result = "invalid"

print(result)
