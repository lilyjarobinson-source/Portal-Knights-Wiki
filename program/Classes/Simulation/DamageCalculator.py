import random
from Hit import hit
class damageCalculator:    
    # change this to use character
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
            "Crit rate" : 20,
            "Crit damage" : 1,
            "Multistrike rate" : 0,
            "Multistrike amount" : 1,
            "Backstab damage" : 1.25,
            "Weaken enemy chance" : 0
        }
        if not hitToCalculate.isAdditionalStrike:
            self.calculatePotionAndEnrageBonus(hitToCalculate, buffController)

            self.calculateHitStartingDamage(hitToCalculate)

            self.calculateWarCryBonus(hitToCalculate, buffController)

        self.calculateTalents(hitToCalculate)

        for i in hitToCalculate.character.extraMultipliers:
            if i in multipliers.keys():
                multipliers[i] += hitToCalculate.character.extraMultipliers[i]
            
        if random.randint(1, 100) <= multipliers["Weaken enemy chance"]:
            hitToCalculate.character.buffs.append(buffController.getBuff("weaken enemy"))

        weakenEnenmyIndex = buffController.checkIfBuffNameInList("weaken enemy", hitToCalculate.character.buffs)
        if weakenEnenmyIndex != -1:
            if hitToCalculate.character.buffs[weakenEnenmyIndex].activeTime > 0:
                hitToCalculate.dmg *= 1.3

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

        self.calculateMultistrikeTalents(hitToCalculate)
        

        return hitToCalculate

    def calculateTalents(self, hitToCalculate):
        match hitToCalculate.character.characterClass:
            case "Warrior":
                if not hitToCalculate.isAdditionalStrike:
                    match hitToCalculate.character.talents[0]:
                        case 0:
                            if hitToCalculate.weapon.wpnType == "Axe":
                                hitToCalculate.dmg *= 1.25
                        case 1:
                            if hitToCalculate.weapon.wpnType == "Hammer":
                                hitToCalculate.dmg *= 1.25
                        case 2:
                            if hitToCalculate.weapon.wpnType in ["Sword", "Saber"]:
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
            case "Warrior":
                if hitToCalculate.character.talents[6] == 0:
                    if not hitToCalculate.isAdditionalStrike:
                        if random.randint(1, 100) <= 10:
                            newHit = hitToCalculate.copy()
                            newHit.isAdditionalStrike = True
                            self.hitList.append(newHit)

    def calculateHitStartingDamage(self, hitToCalculate):
        hitToCalculate.dmg = (hitToCalculate.weapon.baseDmg + hitToCalculate.character.statPoints["melee damage"]) * 0.3 * hitToCalculate.weapon.dmgMult
        
    def calculatePotionAndEnrageBonus(self, hitToCalculate, buffController):
        enrageIndex = buffController.checkIfBuffNameInList("enrage", hitToCalculate.character.buffs)
        if enrageIndex != -1:
            if hitToCalculate.character.buffs[enrageIndex].activeTime > 0:
                hitToCalculate.character.statPoints["melee damage"] = int(hitToCalculate.character.statPoints["melee damage"] * (1.2 + (hitToCalculate.character.attributePoints["strength"] * 0.002)))

    def calculateWarCryBonus(self, hitToCalculate, buffController):
        warCryIndex = buffController.checkIfBuffNameInList("war cry", hitToCalculate.character.buffs)
        if warCryIndex != -1:
            if hitToCalculate.character.buffs[warCryIndex].activeTime > 0:
                hitToCalculate.dmg *= 1.1 + (hitToCalculate.character.attributePoints["strength"] * 0.002)
                

                
