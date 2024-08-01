class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def __str__(self) -> str:
        return f"Length = {self.length} Breadth = {self.breadth}"

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def is_square(self) -> bool:
        return self.length == self.breadth


x = Rectangle(5, 10)
y = Rectangle(10, 20)
print(x)
print(y)
