from typing import List, Dict


def create_dictionary(subjects: List[str], marks: List[int]) -> Dict[str, int]:
    my_dict = {}
    for i in range(len(subjects)):
        my_dict[subjects[i]] = marks[i]
    return my_dict


s = ["chemistry", "english", "hindi"]
m = [56, 43, 121]

ans = create_dictionary(s, m)
print(ans)
