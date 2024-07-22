def islower(user_string: str) -> bool:
    is_lower = False
    is_upper = False
    for ch in user_string:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            is_lower = True
        elif ascii_code >= 65 and ascii_code <= 90:
            is_upper = True
    # if is_lower == True and is_upper == False:
    #     return True
    if is_lower and not is_upper:
        return True
    return False


my_string = "djwakal57439&%$(*)%"
print(islower(my_string))
