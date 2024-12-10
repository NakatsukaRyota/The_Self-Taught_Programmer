class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
    
class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())

square = Square(10)
print(square.calculate_area())