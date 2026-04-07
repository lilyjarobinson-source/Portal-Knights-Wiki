class hit:
    weapon = None
    dmg = 0
    isCriticalStrike = False
    isAdditionalStrike = False

    def __init__(self, character):
        self.weapon = character.weapon
        self.dmg = (self.weapon.baseDmg + character.statPoint["strength"]) * 0.3 * self.weapon.wpnType.dmgMult

    def getDmg(self):
        return int(self.dmg)
