class Animal:
    def set_animal_details(self):
        self.color = input("Enter color = ")
        self.sound = input("Enter sound = ")
        self.height = int(input("Enter Height = "))


class Cat(Animal):
    def set_details(self):
        self.cat_name = input("Enter cat name = ")
        self.cat_owner = input("Enter cat owner name = ")

    def display(self):
        print(f"Cat name = {self.cat_name}")
        print(f"Cat owner = {self.cat_owner}")
        print(f"Color of cat = {self.color}")
        print(f"Sound of cat = {self.sound}")
        print(f"Height of cat = {self.height}")


class Dog(Animal):
    def set_details(self):
        self.set_animal_details()
        self.dog_name = input("Enter dog name = ")
        self.dog_owner = input("Enter dog owner name = ")

    def display(self):
        print(f"Dog name = {self.dog_name}")
        print(f"Dog owner = {self.dog_owner}")
        print(f"Color of dog = {self.color}")
        print(f"Sound of dog = {self.sound}")
        print(f"Height of dog = {self.height}")


d1 = Dog()
d1.set_details()
d1.display()

c1 = Cat()
c1.set_animal_details()
c1.set_details()
c1.display()
