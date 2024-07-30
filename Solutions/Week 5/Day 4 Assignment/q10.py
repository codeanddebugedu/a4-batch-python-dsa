from typing import Dict


def mergeDict(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    result = {}
    result.update(dict1)  # Add all the values of dict1 to result first

    for key, value in dict2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

    return result


d1 = {"a": 54, "b": 11, "c": 90}
d2 = {"a": 100, "b": 200, "d": 56}
print(mergeDict(d1, d2))
