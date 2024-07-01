def marks(sci: int, math: int, eng: int, hindi: int, soc: int):
    # ....
    total = sci + math + eng + hindi + soc
    print(f"Your total marks = {total}")
    percentage = total / 5
    print(f"Your percentage = {percentage}")


marks(15, 60, 70, 80, 90)
