my_string = "abcd$#$%f@%$%$@$#$ABCD7548390"

count = 0
count1 = 0
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        count += 1
    elif ascii_code >= 65 and ascii_code <= 90:
        count1 += 1

for ch in my_string:
    if ord("a") <= ord(ch) <= ord("z"):
        count += 1
    elif "A" <= ch <= "Z":
        count1 += 1


print(f"Total lowercase letters = {count}")
print(f"Total uppercase letters = {count1}")
