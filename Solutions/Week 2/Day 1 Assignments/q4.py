def simple_calculator(a: int, b: int, operation: str):
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)


a = int(input())
b = int(input())
operation = input()

simple_calculator(a, b, operation)
