class Animal:
    def __init__(self) -> None:
        self.color = input("Enter color = ")
        self.sound = input("Enter sound = ")
        self.height = int(input("Enter Height = "))

    def display(self):
        print("----1----")
        print(f"Color = {self.color}")
        print(f"Sound = {self.sound}")
        print(f"Height = {self.height}")


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.dog_name = input("Enter dog name = ")
        self.dog_owner = input("Enter dog owner name = ")

    def display(self):
        print("----2----")
        print(f"Dog name = {self.dog_name}")
        print(f"Dog owner = {self.dog_owner}")
        print(f"Color of dog = {self.color}")
        print(f"Sound of dog = {self.sound}")
        print(f"Height of dog = {self.height}")

    def details(self):
        self.display()
        # super().display()


d1 = Dog()
d1.details()
