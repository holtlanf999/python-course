import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_dmg(self):
        dmglow = self.dmg - 15
        dmghigh = self.dmg + 15
        return random.randrange(dmglow, dmghigh)