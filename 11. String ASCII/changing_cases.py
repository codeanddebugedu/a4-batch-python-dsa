my_string = "abcdABCD%$^&hjkYHOUI"


result = ""

for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        ascii_code -= 32
        result = result + chr(ascii_code)
    else:
        result = result + ch

print(result)
