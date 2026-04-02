class weaponType:
    name = ""
    dmgMult = 0
    attackInterval = 0

class Sword(weaponType):
    def __init__(self):
        self.name = "Sword"
        self.dmgMult = 1
        self.attackInterval = 3/10

class HammerL(weaponType):
    def __init__(self):
        self.name = "Hammer"
        self.dmgMult = 7/3
        self.attackInterval = 7/10

class HammerS(weaponType):
    def __init__(self):
        self.name = "Hammer"
        self.dmgMult = 4/3
        self.attackInterval = 2/5

class Axe(weaponType):
    def __init__(self):
        self.name = "Axe"
        self.dmgMult = 7/3
        self.attackInterval = 7/10

class AxeS(weaponType):
    def __init__(self):
        self.name = "Axe"
        self.dmgMult = 1
        self.attackInterval = 3/10

class Saber(weaponType):
    def __init__(self):
        self.name = "Saber"
        self.dmgMult = 1
        self.attackInterval = 3/10

class Club(weaponType):
    def __init__(self):
        self.name = "Club"
        self.dmgMult = 4/3
        self.attackInterval = 2/5

class Mace(weaponType):
    def __init__(self):
        self.name = "Mace"
        self.dmgMult = 4/3
        self.attackInterval = 2/5

class Knife(weaponType):
    def __init__(self):
        self.name = "Knife"
        self.dmgMult = 11/10
        self.attackInterval = 8/25

class Gauntlet(weaponType):
    def __init__(self):
        self.name = "Gauntlet"
        self.dmgMult = 9/10
        self.attackInterval = 1/4

class Weapon(weaponType):
    def __init__(self):
        self.name = "Weapon"
        self.dmgMult = 1
        self.attackInterval = 2/5

