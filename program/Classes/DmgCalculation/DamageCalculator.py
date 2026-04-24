import random
from Hit import hit
class damageCalculator:
    loadedCharacter = None
    # change this to use character
    def getDamageFromHit(self, character):
        self.loadedCharacter = character
        hitList = [self.calculateDamage(hit(character))]
        for i in range(1, len(hitList)):
            hitList[i] = self.calculateDamage(hitList[i])

        return hitList
        
    def calculateDamage(self, hit):
        multipliers = {
            "mb" : 0,
            "sb" : 0,
            "crR" : 20,
            "crD" : 1,
            "msR" : 0,
            "msA" : 0,
            "weC" : 0,
            "bsD" : 1.25,
        }
        for i in list(hit.weapon.multipliers.keys()):
            multipliers[i] += hit.weapon.multipliers[i]

        if not hit.isCriticalStrike:
            if random.randint(1, 100) <= multipliers["crR"]:
                hit.dmg *= 1.25 * multipliers["crD"]
                hit.isCriticalStrike = True

        return hit
