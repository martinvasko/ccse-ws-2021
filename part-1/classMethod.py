import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


d = Dice(90)
# print(d.roll())
print(random.randint(1, 90))
