class hit:
    weapon = None
    dmg = 0
    isCriticalStrike = False
    isAdditionalStrike = False

    def __init__(self, weapon):
        self.weapon = weapon
        self.dmg = weapon.baseDmg * 0.3 * weapon.wpnType.dmgMult
