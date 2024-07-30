def max_frequency(lst: str) -> None:
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


s = "helllo world"
max_frequency(s)
