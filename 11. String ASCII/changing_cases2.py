# Swapcase
# Uppercase -> Lowercase
# Lowercase -> Uppercase

my_string = "DHhdjka^&#$(*)$   ...///;;''DADWAHKjyuihdwakj"
result = ""
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        ascii_code -= 32
        result = result + chr(ascii_code)
    elif ascii_code >= 65 and ascii_code <= 90:
        ascii_code += 32
        result = result + chr(ascii_code)
    else:
        result = result + ch
print(result)
