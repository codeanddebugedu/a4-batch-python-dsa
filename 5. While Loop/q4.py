"""
Ask a start number from user = 6
Ask a end number from user = 15

6 7 8...14 15


Ask a start number from user = 20
Ask a end number from user = 3

3 4 5 6..19 20
"""

st = int(input("Enter start = "))  # 20
en = int(input("Enter end = "))  # 20

if st < en:
    i = st
    j = en
    while i <= j:
        print(i, end=" ")
        i += 1
else:
    i = en
    j = st
    while i <= j:
        print(i, end=" ")
        i += 1
