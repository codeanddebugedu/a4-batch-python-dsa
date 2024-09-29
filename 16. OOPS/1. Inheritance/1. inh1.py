class Dog:
    def set_details(self):
        self.dog_name = input("Enter dog name = ")
        self.dog_owner = input("Enter dog owner name = ")
        self.color = input("Enter color = ")
        self.sound = input("Enter sound = ")
        self.height = int(input("Enter Height = "))

    def display(self):
        print(f"Dog name = {self.dog_name}")
        print(f"Dog owner = {self.dog_owner}")
        print(f"Dog color = {self.color}")
        print(f"Dog sound = {self.sound}")
        print(f"Dog height = {self.height}")


class Cat:
    def set_details(self):
        self.cat_name = input("Enter cat name = ")
        self.cat_owner = input("Enter cat owner name = ")
        self.color = input("Enter color = ")
        self.sound = input("Enter sound = ")
        self.height = int(input("Enter Height = "))

    def display(self):
        print(f"Cat name = {self.cat_name}")
        print(f"Cat owner = {self.cat_owner}")
        print(f"Cat color = {self.color}")
        print(f"Cat sound = {self.sound}")
        print(f"Cat height = {self.height}")


d1 = Dog()
d1.set_details()
d1.display()

c1 = Cat()
