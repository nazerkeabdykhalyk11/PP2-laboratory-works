class Shape:
    def __init__(self):
        self.name = "Shape"

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = "Square"

    def area(self):
        return self.length ** 2

square = Square(4)
print(f"The area of the {square.name} is: {square.area()}")
