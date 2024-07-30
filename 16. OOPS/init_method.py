class Student:
    # Magic/Dunder Methods
    def __init__(
        self,
        idd: int,
        name: str,
        age: int,
        gender: str,
        address: str = "",
        school: str = "SDJ",
    ):
        self.idd = idd
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.school = school

    # def __init__(self):
    #     self.idd = int(input("Enter ID = "))
    #     self.name = input("Enter name = ")
    #     self.age = int(input("Enter age = "))
    #     self.gender = input("Enter gender = ")
    #     self.address = "Surat"

    def updateName(self, new_name) -> None:
        self.name = new_name

    def display(self):
        print(f"ID = {self.idd}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Address = {self.address}")


s1 = Student(1, "Anirudh", 18, "Male")
# s1 = Student(age=12, idd=23, name="Anirudh", gender="Male")
s1.display()
s1.updateName("XYZ")
s1.display()
