class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"
    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side
    
    def change_size(self, num):
        self.side += num

rectangle = Rectangle(10, 20)
print(rectangle.what_am_i())

square = Square(10)
print(square.what_am_i())