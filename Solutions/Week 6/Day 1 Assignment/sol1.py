from typing import Dict, List

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}


# Q1: Print all the marks of each student in a readable format.
def print_all_marks(details: Dict[str, List[int]]):
    for student, marks in details.items():
        # print(f"{student}: {', '.join(map(str, marks))}")
        print(f"{student}: {', '.join(str(m) for m in marks)}")


# print_all_marks(details)


# Q2: Print the student name and their corresponding highest marks.
def print_highest_marks(details: Dict[str, List[int]]):
    for student, marks in details.items():
        highest_mark = marks[0]
        for mark in marks:
            if mark > highest_mark:
                highest_mark = mark
        print(f"{student}: {highest_mark}")


# print_highest_marks(details)


# Q3: Find and print the student(s) with the highest individual score.
def print_top_scorer(details: Dict[str, List[int]]):
    highest_score = max(max(marks) for marks in details.values())
    for student, marks in details.items():
        if highest_score in marks:
            print(f"The highest mark is {highest_score}, scored by {student}.")


# print_top_scorer(details)


# Q4: Calculate and print the average marks of each student.
# def print_average_marks(details: Dict[str, List[int]]):
#     for student, marks in details.items():
#         average = sum(marks) / len(marks)
#         print(f"{student}: {average:.2f}")
def print_average_marks(details: Dict[str, List[int]]):
    for student, marks in details.items():
        total = 0
        count = 0
        for mark in marks:
            total += mark
            count += 1
        average = total / count
        print(f"{student}: {average:.2f}")


# print_average_marks(details)


# Q5: Print the name of the student who has the highest average marks.
# def print_highest_average(details: Dict[str, List[int]]):
#     highest_average = 0
#     top_student = ""
#     for student, marks in details.items():
#         average = sum(marks) / len(marks)
#         if average > highest_average:
#             highest_average = average
#             top_student = student
#     print(
#         f"The highest average marks are {highest_average:.2f}, scored by {top_student}."
#     )
def print_highest_average(details: Dict[str, List[int]]):
    highest_average = 0
    top_student = ""
    for student, marks in details.items():
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
        f"The highest average marks are {highest_average:.2f}, scored by {top_student}."
    )


# print_highest_average(details)


# Q6: Print the total number of marks entries for each student.
def print_marks_count(details: Dict[str, List[int]]):
    for student, marks in details.items():
        print(f"{student:}: {len(marks)}")


# print_marks_count(details)


# Q7: Identify and print the name(s) of the student(s) who have scored more than a specified number of marks.
def print_students_above_threshold(details: Dict[str, List[int]], threshold: int):
    for student, marks in details.items():
        above_threshold = [mark for mark in marks if mark > threshold]
        if above_threshold:
            print(f"{student}: {above_threshold}")


# print_students_above_threshold(details, 75)
