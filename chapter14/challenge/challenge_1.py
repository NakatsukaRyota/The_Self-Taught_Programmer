class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return f"{self.side} by {self.side} by {self.side} by {self.side}"

square = Square(10)
print(square)




    