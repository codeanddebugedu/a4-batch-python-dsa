from typing import List


class Student:
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def updateDetails(self, new_name=None, age=None, gender=None) -> None:
        # if new_name != None:
        #     self.name = new_name
        if new_name:
            self.name = new_name
        if age:
            self.age = age
        if gender:
            self.gender = gender

    def total(self) -> int:
        # return sum(self.marks)
        t = 0
        for m in self.marks:
            t = t + m
        return t

    def display(self):
        print(f"Rol No = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"Marks = {self.marks}\n\n")


student_details: List[Student] = []

while True:
    print("1) Add a student")
    print("2) Remove a student")
    print("3) Display all student details")
    print("4) Update student details")
    print("5) Display a student detail")
    print("6) Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        roll_no = int(input("Enter roll no = "))
        name = input("Enter name = ")
        age = int(input("Enter age = "))
        gender = input("Enter gender = ")
        no_of_s = int(input("Enter number of subjects = "))
        marks = []
        for _ in range(no_of_s):
            m = int(input("Enter marks = "))
            marks.append(m)

        x = Student(roll_no, name, age, gender, marks)
        student_details.append(x)

    elif choice == 2:
        rno = int(input("Enter student roll number you want to delete = "))
        student_index = -1
        for i in range(0, len(student_details)):
            if student_details[i].roll_no == rno:
                student_index = i
                break
        if student_index == -1:
            print("Student not found")
        else:
            student_details.pop(student_index)
            print("Student deleted\n\n")

    elif choice == 3:
        if len(student_details) == 0:
            print("No students found")
        else:
            for stu in student_details:
                stu.display()
    elif choice == 4:
        rno = int(input("Enter student roll number you want to update details = "))
        for stu in student_details:
            if stu.roll_no == rno:
                n_name = input("Enter new name = ")
                n_age = int(input("Enter new age = "))
                n_gender = input("Enter new gender = ")
                stu.updateDetails(n_name, n_age, n_gender)
                break
        else:
            print("No student found with that roll number")
    elif choice == 5:
        rno = int(input("Enter student roll number you want to search for = "))
        for stu in student_details:
            if stu.roll_no == rno:
                stu.display()
                break
        else:
            print("No student found with that roll number")

    elif choice == 6:
        break
    else:
        print("Invalid Choice")
