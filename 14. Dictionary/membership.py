from typing import Dict


marks: Dict[str, int] = {
    "history": 78,
    "science": 16,
    "computer": 99,
    "chemistry": 65,
    "sst": 25,
}

print(25 in marks)
print("history" in marks)
print("historyy" in marks)
