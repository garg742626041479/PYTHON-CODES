#demostrate following operations : simple multiplication inheritance

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Rectangle(Shape):
    pass

class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

rectangle = Rectangle(5, 10)
square = Square(5)

print(f"Rectangle area: {rectangle.area()}")
print(f"Square area: {square.area()}")