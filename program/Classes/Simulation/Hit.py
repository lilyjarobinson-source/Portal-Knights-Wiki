class hit:
    def __init__(self, character):
        self.isCriticalStrike = False
        self.isAdditionalStrike = False
        self.isEnemyOfParentHitWeak = False
        self.weapon = character.weapon
        self.character = character
        self.dmg = (self.weapon.baseDmg + self.character.statPoints["melee damage"]) * 0.3 * self.weapon.dmgMult

    def getDmg(self):
        return int(self.dmg)

    def copy(self):
        newHit = hit(self.character)
        newHit.isCriticalStrike = self.isCriticalStrike
        newHit.isAdditionalStrike = self.isAdditionalStrike
        newHit.dmg = self.dmg
        return newHit
        
