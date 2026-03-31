class weapon:
    name = ""
    requiredLevel = 0
    baseDmg = 0
    wpnType = None
    multipliers = {}

    def toString(self):
        return f"{self.name} {self.requiredLevel} {self.baseDmg} {self.wpnType.name} {self.multipliers}"
