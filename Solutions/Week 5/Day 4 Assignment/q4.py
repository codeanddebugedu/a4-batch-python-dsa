def does_key_exists(dictnry, key) -> bool:
    return key in dictnry


d = {"anirudh": 45, 56: 78, "gender": "Male", 11: 22}
print(does_key_exists(d, "xyz"))
