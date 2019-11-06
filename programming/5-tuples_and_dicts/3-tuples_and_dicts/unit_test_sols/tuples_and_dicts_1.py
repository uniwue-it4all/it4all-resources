from typing import Dict, List, Tuple


def tuple_list_to_dict(my_list: List[Tuple[str, int]]) -> Dict[str, int]:
    result: Dict[str, int] = {}

    for key, value in my_list:
        if value not in result:
            result[str(value)] = int(key)

    return result


def intersect_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, Tuple[int, int]]:
    result: Dict[str, Tuple[int, int]] = {}

    for key, value in dict1.items():
        if key in dict2:
            result[key] = (value, dict2[key])

    return result
