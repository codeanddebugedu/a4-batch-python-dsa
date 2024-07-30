class Student:
    # Methods
    def setDetails(self):
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.address = "Surat"

    def display(self):
        print(f"ID = {self.idd}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Address = {self.address}")


s1 = Student()
s1.setDetails()
s1.display()
