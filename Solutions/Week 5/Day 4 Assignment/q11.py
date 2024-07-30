from typing import Dict


def removeKeysWithValueGreaterThanK(dictnry: Dict, k: int):
    result = {}
    for key, value in dictnry.items():
        if isinstance(value, int) or isinstance(value, float):
            if value < k:
                result[key] = value
        else:
            result[key] = value
    return result
