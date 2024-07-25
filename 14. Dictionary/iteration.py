marks = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}

for k in marks:
    # print(k)
    # print(marks[k])
    print(f"Key = {k}, Value = {marks[k]}")

total = 0
for k in marks:
    total = total + marks[k]

print(total)
