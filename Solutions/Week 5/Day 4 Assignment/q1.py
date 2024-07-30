from typing import Dict


def store_details() -> Dict[str, int]:
    result = {}
    number_of_subjects = int(input("Enter number of subjects = "))
    for _ in range(number_of_subjects):
        name = input("Enter subject name = ")
        marks = int(input("Enter subject marks = "))
        # result.update({name: marks})
        result[name] = marks
    return result


print(store_details())
