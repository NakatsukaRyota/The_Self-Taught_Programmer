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
    
    def change_size(self, num):
        self.side += num

square = Square(10)
print(square.side)

square.change_size(-5)
print(square.side)