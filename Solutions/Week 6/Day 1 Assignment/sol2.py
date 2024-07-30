from typing import Dict, List

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


def print_name_and_age(details: Dict[str, Dict]):
    for student, info in details.items():
        print(f"{student}: {info['age']}")


def print_adults(details: Dict[str, Dict]):
    for student, info in details.items():
        if info["adult"]:
            print(student)


def print_average_marks(details: Dict[str, Dict]):
    for student, info in details.items():
        marks = info["marks"]
        total = 0
        count = 0
        for mark in marks:
            total += mark
            count += 1
        average = total / count
        print(f"{student}: {average:.2f}")


def print_highest_marks(details: Dict[str, Dict]):
    for student, info in details.items():
        marks = info["marks"]
        highest_mark = marks[0]
        for mark in marks:
            if mark > highest_mark:
                highest_mark = mark
        print(f"{student}: {highest_mark}")


def print_students_with_more_than_three_marks(details: Dict[str, Dict]):
    for student, info in details.items():
        if len(info["marks"]) > 3:
            print(student)


def print_total_marks(details: Dict[str, Dict]):
    for student, info in details.items():
        total_marks = 0
        for mark in info["marks"]:
            total_marks += mark
        print(f"{student}: {total_marks}")


def print_youngest_student(details: Dict[str, Dict]):
    youngest_age = None
    youngest_student = ""
    for student, info in details.items():
        age = info["age"]
        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_student = student
    print(f"The youngest student is {youngest_student}, age {youngest_age}.")


def print_highest_average(details: Dict[str, Dict]):
    highest_average = 0
    top_student = ""
    for student, info in details.items():
        marks = info["marks"]
        total = 0
        count = 0
        for mark in marks:
            total += mark
            count += 1
        average = total / count
        if average > highest_average:
            highest_average = average
            top_student = student
    print(
        f"The student with the highest average marks is {top_student} with an average of {highest_average:.2f}."
    )


# print_name_and_age(details)
# print_adults(details)
# print_average_marks(details)
# print_highest_marks(details)
# print_students_with_more_than_three_marks(details)
# print_total_marks(details)
# print_youngest_student(details)
# print_highest_average(details)
