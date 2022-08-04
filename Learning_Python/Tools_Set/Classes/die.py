
from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(f"sides: {self.sides} number: {number}")

my_die1 = Die(6)
my_die2 = Die(10)
my_die3 = Die(20)
my_die1.roll_die()
my_die2.roll_die()
my_die3.roll_die()



