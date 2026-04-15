class weapon:
    def __init__(self):
        self.name = ""
        self.requiredLevel = 0
        self.baseDmg = 0
        self.wpnType = None
        self.multipliers = {}
        self.perk = ""

    def toString(self):
        return f"{self.name} {self.requiredLevel} {self.baseDmg} {self.wpnType.name} {self.multipliers} {self.perk}"
