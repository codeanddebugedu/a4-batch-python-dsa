from typing import Dict


def updateDict(dictnry: Dict) -> Dict:
    new_dict = {}
    for key, value in dictnry.items():
        if isinstance(value, str):
            new_dict[key] = value
            # new_dict.update({key: value})
    return new_dict


my_dict = {"a": "b", "z": 12, "adult": True, "gender": "Male"}
new_d = updateDict(my_dict)
print(new_d)
