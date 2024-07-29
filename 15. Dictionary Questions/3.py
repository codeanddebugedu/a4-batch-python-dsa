from typing import List, Dict

"""
Anirudh has scored 340 marks
Sanjay has scored 987 marks
..
..
"""


# def displayDetails(my_dict: Dict[str, List[int]]) -> None:
#     for name, marks in my_dict.items():
#         # print(f"{name} has scored {sum(marks)} marks")
#         total = 0
#         for i in range(0, len(marks)):
#             total = total + marks[i]
#         print(f"{name} has scored {total} marks")


def displayDetails(my_dict: Dict[str, List[int]]) -> None:
    for key in my_dict:
        total = 0
        for i in range(0, len(my_dict[key])):
            total = total + my_dict[key][i]
        print(f"{key} has scored {total} marks")


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

displayDetails(details)
