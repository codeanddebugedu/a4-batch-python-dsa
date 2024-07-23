def is_alphanumeric(s: str) -> bool:
    for char in s:
        if not (("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9")):
            return False
    return True
