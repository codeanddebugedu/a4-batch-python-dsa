from typing import Dict


marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}
print(marks)


marks["sst"] = 50
marks["english"] = 100
# marks.update({"english": 100})
# marks.update({"sst": 50})
print(marks)
