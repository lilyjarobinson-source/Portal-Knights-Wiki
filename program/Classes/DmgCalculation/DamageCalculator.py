import random
from Hit import hit
class damageCalculator:
    # change this to use character
    def getDamageFromHit(self, character):
        hitList = [self.calculateDamage(hit(character))]
        for i in range(1, len(hitList)):
            hitList[i] = self.calculateDamage(hitList[i])

        return hitList
        
    def calculateDamage(self, hit):
        multipliers = {
            "Crit rate" : 20,
            "Crit damage" : 1,
            "Multistrike rate" : 0,
            "Multistrike amount" : 0,
            "Weaken enemy chance" : 0,
            "Backstab damage" : 1.25,
        }
        for i in list(hit.weapon.multipliers.keys()):
            multipliers[i] += hit.weapon.multipliers[i]

        if not hit.isCriticalStrike:
            if random.randint(1, 100) <= multipliers["Crit rate"]:
                hit.dmg *= 1.25 * multipliers["Crit damage"]
                hit.isCriticalStrike = True

        return hit
