class Father:
    def __init__(self) -> None:
        print("Father INIT")
        self.father_name = input("Enter father name = ")


class Mother:
    def __init__(self) -> None:
        print("Mother INIT")
        self.mother_name = input("Enter mother name = ")


class Son(Father, Mother):
    def __init__(self) -> None:
        Mother.__init__(self)
        Father.__init__(self)
        print("Son INIT")
        self.name = input("Enter name = ")

    def display(self):
        print(f"Father name = {self.father_name}")
        print(f"Mother name = {self.mother_name}")
        print(f"My name = {self.name}")


s1 = Son()
s1.display()
