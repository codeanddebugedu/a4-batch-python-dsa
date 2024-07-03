"""
Ask a start number from user = 6
Ask a end number from user = 15

start to end
6 7 8 9....14 15

"""

# Input Parameters
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
j = end

while i <= j:
    print(i, end=" ")
    i += 1
print()
# while start <= end:
#     print(start, end=" ")
#     start += 1
