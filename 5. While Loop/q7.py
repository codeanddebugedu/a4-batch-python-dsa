# 1 to 10,,,total (1+2+3+4...+9+10)
st = int(input("Enter st number = "))
en = int(input("Enter en number = "))
i = st
total = 0
while i <= en:
    total = total + i
    i += 1
print(total)
