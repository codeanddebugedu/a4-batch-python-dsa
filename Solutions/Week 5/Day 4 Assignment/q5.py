from typing import Dict


def merge_dict(dict1: Dict, dict2: Dict) -> Dict:
    # dict1.update(dict2)
    for key, value in dict2.items():
        # dict1.update({key: value})
        dict1[key] = value
    return dict1


d1 = {"a": 54, "b": 11, "c": 90}
d2 = {"a": 100, "b": 200, "d": 56}

print(merge_dict(d1, d2))
