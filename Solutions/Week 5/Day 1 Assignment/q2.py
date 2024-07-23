def to_uppercase(s: str) -> str:
    uppercase_string = ""
    for char in s:
        if "a" <= char <= "z":
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string


my_string = "aB677^&*hx"

print(to_uppercase(my_string))
