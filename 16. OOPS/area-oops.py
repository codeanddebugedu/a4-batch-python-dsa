class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def is_square(self) -> bool:
        return self.length == self.breadth
        # if self.length == self.breadth:
        #     return True
        # return False


x = Rectangle(5, 10)  # <---- init
print(x.area())
print(x.perimeter())
print(x.is_square())
