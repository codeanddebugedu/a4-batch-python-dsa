def remove_non_alphabetic(s: str) -> str:
    result = ""
    for char in s:
        if ("a" <= char <= "z") or ("A" <= char <= "Z") or char == " ":
            result += char
    return result
