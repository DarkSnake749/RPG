class Item:
    def __init__(self, name, dura):
        self.name = name
        self.dura = dura
    def use_dura(self):
        self.dura -= 1

class Weapon(Item):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage