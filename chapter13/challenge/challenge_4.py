class Horse:
    def __init__(self, name, weight, rider):
        self.name = name
        self.weight = weight
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("Nakatsuka")
horse = Horse("yako", 300, rider)

print(horse.rider.name)