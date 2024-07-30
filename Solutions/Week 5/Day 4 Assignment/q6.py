from typing import Dict


def multiply_factor(dictionary: Dict, factor: int) -> Dict:
    new_dict = dictionary.copy()  # We dont want to change the original one
    for key, value in new_dict.items():
        if isinstance(value, int):
            new_dict[key] = value * factor
    return new_dict


d = {"a": 56, "b": "hello", "c": 55.67, "d": True, "e": 100}

print(multiply_factor(d, 3))
