"""
Anirudh has scored 455 highest marks
Muskan has scored 99 highest marks
"""

details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

# print(details["Muskan"]["gender"])
# print(details["Muskan"]["marks"][-1])
# for name, info in details.items():
#     if info["adult"] == True:
#         print(name, info["age"])

for key in details:
    total = 0
    for mark in details[key]["marks"]:
        total += mark
    print(f"{key} has scored {total} marks")

# for name, info in details.items():
#     # print(f"{name} has scored {sum(info['marks'])}")
#     total = 0
#     for mark in info["marks"]:
#         total = total + mark
#     print(f"{name} has scored {total} marks")
