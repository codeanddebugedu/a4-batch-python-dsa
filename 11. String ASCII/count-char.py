def count_char(user_String: str):
    aplhabets = 0
    digits = 0
    spaces = 0
    symbols = 0
    for ch in user_String:
        ascii_code = ord(ch)
        if (97 <= ascii_code <= 122) or (65 <= ascii_code <= 90):
            aplhabets += 1
        elif ord(ch) >= ord("0") and ascii_code <= 57:
            digits += 1
        elif ord(ch) == ord(" "):
            spaces += 1
        else:
            symbols += 1

    print(
        f"Aplhabets = {aplhabets}, digits = {digits}, spaces = {spaces}, symbols = {symbols}"
    )


my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
# Count alphabets, digits, spaces and symbols.
count_char(my_string)
