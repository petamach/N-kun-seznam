import random
class Warrior:

    def __init__(self, name):
        self.name = name
        self.lives = 12
        self.defence = 5
        self.attack = random.randint(3,7)
    def zautoc(self, warr):
        att = self.attack + random.randint(2,4)
        print(f"{self.name} zautoci za {att}")
        deff = warr.defence + random.randint(3,5)
        print(f"{self.name} se brani za {deff}")
        if att > deff:
            warr.lives -= abs(att - deff)




def arena(war1,war2):
    while war1.lives > 0 and war2.lives > 0:
        war1.zautoc(war2)
        if (war2.lives <= 0):
            print(f"Zvitezil valecnik {war1.name}")
            return
        else:
            war2.zautoc(war1)
    print(f"Zvitezil valecnik {war2.name}")


if __name__ == "__main__":
    war1 = Warrior("Kundolap")
    war2 = Warrior("Zlobr")
    arena(war1,war2)
        
