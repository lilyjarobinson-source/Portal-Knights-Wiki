class armour:
    name = ""
    requiredLevel = 0
    baseDefence = 0
    classRestriction = ""
    slot = ""
    multipliers = {}
    buff = ""

    def toString(self):
        return f"{self.name} {self.requiredLevel} {self.baseDefence} {self.classRestriction} {self.slot} {self.multipliers} {self.buff}"
