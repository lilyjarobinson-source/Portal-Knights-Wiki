import random
from Hit import hit
class damageCalculator:
    multipliers = [
        "Crit rate",
        "Crit damage",
        "Multistrike rate",
        "Multistrike amount",
        "Weaken enemy chance",
        "Backstab damage"
    ]
    # change this to use character
    def __init__(self):
        self.hitList = []
    def getDamageFromHit(self, character):
        self.hitList = []
        hitCalculated = self.calculateDamage(hit(character))
        self.hitList.insert(0, hitCalculated)
        for i in range(1, len(self.hitList)):
            self.hitList[i] = self.calculateDamage(self.hitList[i])

        return self.hitList
        
    def calculateDamage(self, hitToCalculate):
        multipliers = {
            "Crit rate" : 20,
            "Crit damage" : 1,
            "Multistrike rate" : 0,
            "Multistrike amount" : 1,
            "Weaken enemy chance" : 0,
            "Backstab damage" : 1.25,
        }
        for i in hitToCalculate.weapon.multipliers:
            if i in damageCalculator.multipliers:
                multipliers[i] += hitToCalculate.weapon.multipliers[i]
        for i in hitToCalculate.character.armourMultipliers:
            multipliers[i] += hitToCalculate.character.armourMultipliers[i]
            
        if random.randint(1, 100) <= multipliers["Weaken enemy chance"]:
            hitToCalculate.character.buffTimers.update({"Weaken enemy" : 3})

        if "Weaken enemy" in hitToCalculate.character.buffTimers:
            if hitToCalculate.character.buffTimers["Weaken enemy"] > 0:
                hitToCalculate.dmg *= 1.3
            else:
                hitToCalculate.character.buffTimers.pop("Weaken enemy")

        if not hitToCalculate.isCriticalStrike and not hitToCalculate.isAdditionalStrike:
            if random.randint(1, 100) <= multipliers["Crit rate"]:
                hitToCalculate.dmg *= 1.25 * multipliers["Crit damage"]
                hitToCalculate.isCriticalStrike = True

        if not hitToCalculate.isAdditionalStrike:
            if random.randint(1, 100) <= multipliers["Multistrike rate"]:
                for i in range(int(multipliers["Multistrike amount"])):
                    newHit = hitToCalculate.copy()
                    newHit.isAdditionalStrike = True
                    self.hitList.append(newHit)
        

        return hitToCalculate
