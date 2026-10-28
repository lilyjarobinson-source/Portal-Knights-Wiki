import random
from Hit import hit
class damageCalculator:
    def __init__(self):
        self.hitList = []
    
    def getDamageFromHit(self, characterController, buffController, character):
        characterController.generateStatPoints(character)
        self.hitList = []
        hitCalculated = self.calculateDamage(hit(character), buffController)
        self.hitList.insert(0, hitCalculated)
        for i in range(1, len(self.hitList)):
            self.hitList[i] = self.calculateDamage(self.hitList[i], buffController)

        return self.hitList
        
    def calculateDamage(self, hitToCalculate, buffController):
        multipliers = {
            "crit rate" : 20,
            "crit damage" : 1,
            "multistrike rate" : 0,
            "multistrike amount" : 1,
            "backstab damage" : 1.25,
            "weaken enemy chance" : 0
        }
        if not hitToCalculate.isAdditionalStrike:
            self.calculateHitStartingDamage(hitToCalculate)

            self.calculateWarCryBonus(hitToCalculate, buffController)
            #print(hitToCalculate.character.statPoints)

        self.calculateTalents(hitToCalculate)

        for i in hitToCalculate.character.extraMultipliers:
            if i in multipliers.keys():
                multipliers[i] += hitToCalculate.character.extraMultipliers[i]
            
        if random.randint(1, 100) <= multipliers["weaken enemy chance"]:
            buffController.applyBuffName(hitToCalculate.character, "weaken enemy")

        if buffController.characterHasBuffName(hitToCalculate.character, "weaken enemy"):
            hitToCalculate.dmg *= 1.3

        if not hitToCalculate.isCriticalStrike and not hitToCalculate.isAdditionalStrike:
            if random.randint(1, 100) <= multipliers["crit rate"]:
                hitToCalculate.dmg *= 1.25 * multipliers["crit damage"]
                hitToCalculate.isCriticalStrike = True

        if not hitToCalculate.isAdditionalStrike:
            if random.randint(1, 100) <= multipliers["multistrike rate"]:
                for i in range(int(multipliers["multistrike amount"])):
                    newHit = hitToCalculate.copy()
                    newHit.isAdditionalStrike = True
                    self.hitList.append(newHit)

        self.calculateMultistrikeTalents(hitToCalculate)
        

        return hitToCalculate

    def calculateTalents(self, hitToCalculate):
        match hitToCalculate.character.characterClass:
            case "warrior":
                if not hitToCalculate.isAdditionalStrike:
                    match hitToCalculate.character.talents[0]:
                        case 0:
                            if hitToCalculate.weapon.wpnType == "axe":
                                hitToCalculate.dmg *= 1.25
                        case 1:
                            if hitToCalculate.weapon.wpnType == "hammer":
                                hitToCalculate.dmg *= 1.25
                        case 2:
                            if hitToCalculate.weapon.wpnType in ["sword", "saber"]:
                                hitToCalculate.dmg *= 1.25
                    if hitToCalculate.character.talents[1] == 2:
                        hitToCalculate.dmg *= 1.15
                if hitToCalculate.character.talents[4] == 0:
                    if hitToCalculate.isAdditionalStrike:
                        hitToCalculate.character.hitCounter += 1
                    elif hitToCalculate.character.hitCounter > 3:
                        hitToCalculate.character.hitCounter = 1
                        hitToCalculate.dmg *= 1.5
                    else:
                        hitToCalculate.character.hitCounter += 1

    def calculateMultistrikeTalents(self, hitToCalculate):
        match hitToCalculate.character.characterClass:
            case "warrior":
                if hitToCalculate.character.talents[6] == 0:
                    if not hitToCalculate.isAdditionalStrike:
                        if random.randint(1, 100) <= 10:
                            newHit = hitToCalculate.copy()
                            newHit.isAdditionalStrike = True
                            self.hitList.append(newHit)

    def calculateHitStartingDamage(self, hitToCalculate):
        hitToCalculate.dmg = (hitToCalculate.weapon.baseDmg + hitToCalculate.character.statPoints["melee damage"]) * 0.3 * hitToCalculate.weapon.dmgMult

    def calculateWarCryBonus(self, hitToCalculate, buffController):
        if buffController.characterHasBuffName(hitToCalculate.character, "war cry"):
            hitToCalculate.dmg *= 1.1 + (hitToCalculate.character.attributePoints["strength"] * 0.002)
                

                
