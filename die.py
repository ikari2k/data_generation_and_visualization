from random import randint


class Die:
    """Class representing single game die"""

    def __init__(self, num_sides=6):
        """We define die with 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """Return number 1-6"""
        return randint(1, self.num_sides)
