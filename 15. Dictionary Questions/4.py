from typing import List, Dict


def maxMarks(my_dict: Dict[str, List[int]]) -> None:
    maxi = 0
    maxi_student_name = ""
    for name, marks in my_dict.items():
        total = 0
        for i in range(0, len(marks)):
            total = total + marks[i]
        if total > maxi:
            maxi = total
            maxi_student_name = name
    print(maxi_student_name, maxi)


details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

maxMarks(details)
