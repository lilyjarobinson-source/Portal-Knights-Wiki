class weapon:
    def __init__(self):
        self.name = ""
        self.classRestriction = ""
        self.requiredLevel = 0
        self.baseDmg = 0
        self.wpnType = ""
        self.multipliers = {}
        self.buff = ""
        self.dmgMult = 0
        self.hitInterval = 0
        

    def toString(self):
        return f"{self.name} {self.requiredLevel} {self.baseDmg} {self.wpnType.name} {self.multipliers} {self.perk}"
