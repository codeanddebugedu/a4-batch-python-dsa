my_string = "ahgghgtzzhjsklhhhgaaaaaauaa"
my_dict = {}

for num in my_string:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
max_freq = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_freq:
        max_freq = my_dict[key]
        max_element = key

print(max_element)
print(max_freq)
