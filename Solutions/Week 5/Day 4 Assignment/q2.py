from typing import List


def max_frequency(lst: List[int]) -> None:
    max_freq = 0
    max_freq_element = None
    my_dict = {}
    for num in lst:
        my_dict[num] = my_dict.get(num, 0) + 1

    for ele, freq in my_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_element = ele

    print(f"{max_freq_element} has the highest frequency of {max_freq}")


my_list = [1, 4, 5, 6, 3, 8, 6, 4, 5, 3, 4, 5, 1, 3, 4, 4, 5, 7, 4, 4, 4]
max_frequency(my_list)
