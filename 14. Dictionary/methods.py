from typing import Dict

marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}
print(marks)

# marks.clear()
# print(marks["historyy"])
# print(marks.get("shjgwahdgajwhkdgawj", 0))
marks.pop("history")

print(marks)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 1, "d": 4, "a": 100}

dict1.update(dict2)
print(dict1)
