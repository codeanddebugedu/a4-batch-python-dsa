my_string = "aeghbioudh"

total = 0
for ch in my_string.lower():
    # if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    #     total += 1
    if ch in "aeiouAEIOU":
        total += 1

print(total)
