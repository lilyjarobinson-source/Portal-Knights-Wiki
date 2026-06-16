import sys, random
from WeaponController import weaponController
from ArmourController import armourController
from BuffController import buffController
from Character import character
class characterController:
    multipliers = [
        "Crit rate",
        "Crit damage",
        "Multistrike rate",
        "Multistrike amount",
        "Weaken enemy chance",
        "Backstab damage"
    ]
    def new(self):
        c = character()
        self.generateCharacterId(c)
        w = weaponController()
        c.weapon = w.fist()
        return c

    def generateCharacterId(self, c):
        #print("generating character id")
        contents = self.loadCharFileContents()
        newId = self.generateNewId()
        idIsTaken = True
        while idIsTaken:
            idIsTaken = False
            for i in contents:
                if i.split(",")[0] == newId:
                    idIsTaken = True
                    newId = self.generateNewId()
                    break
        c.characterId = newId
        #print("finished generating character id")

    def generateNewId(self):
        newId = ""
        for i in range(6):
            newId += str(random.randint(0, 9))
        return newId

    def getAllCharacters(self):
        #print("getting all characters")
        characters = []
        for i in self.loadCharFileContents():
            characters.append(self.getCharacterDataFromSaveLine(i))
        #print("finished getting all characters")
        return characters

    def loadCharFileContents(self):
        #print("loading characters file as string array")
        classPath = __file__.split("program")[0]
        try:
            file = open(classPath + "userdata\\characters.txt", "r")
            contents = file.read()
            file.close()
        except:
            file = open(classPath + "userdata\\characters.txt", "w")
            file.write("")
            file.close()
            return []
        #print("finished loading characters file as string array")
        return contents.split("\n")[:-1]

    def getCharacterDataFromSaveLine(self, line):
        
        w = weaponController()
        a = armourController()
        
        #print("getting character data from line")
        line = line.split(",")[:-1]
        c = character()
        c.characterId = line[0]
        c.name = line[1]
        
        
        c.level = int(line[3])
        c.characterClass = line[4]
        w.loadWeapons(c)
        c.weapon = w.getWeapon(line[2])
        a.loadArmourPieces(c)
        c.colour = line[5]
        keyList = list(c.armour.keys())
        for i in range(len(keyList)):
            c.armour[keyList[i]] = a.getArmourPiece(line[6 + i])
        attrKeyList = list(c.attributePoints.keys())
        for i in range(6):
            c.attributePointDistribution[attrKeyList[i]] = int(line[12 + i])
        for i in range(7):
            c.talents[i] = int(line[18 + i])
        self.getBuffDataFromList(c, line[25:])
        #print("finished getting character data from line")
        return c

    def getBuffDataFromList(self, c, buffData):
        for i in buffData:
            c.startingBuffs.append(i)           

    def saveCharacterData(self, characterToSave):
        #print("saving character data")
        classPath = __file__.split("program")[0]
        contents = self.loadCharFileContents()
        charFound = False
        for i in range(len(contents)):
            if contents[i].split(",")[0] == characterToSave.characterId:
                contents[i] = self.convertCharacterToSaveFormat(characterToSave)
                charFound = True
                break

        if not charFound:
            contents.append(self.convertCharacterToSaveFormat(characterToSave))

        content = ""
        for i in contents:
            content += i + "\n"
        #'''
        file = open(classPath + "userdata\\characters.txt", "w")
        file.write(content)
        file.close()
        #'''
        #print("finished saving character data")

    def saveCharacters(self, characters):
        #print("saving characters")
        classPath = __file__.split("program")[0]
        content = ""
        for i in characters:
            content += self.convertCharacterToSaveFormat(i) + "\n"
        #'''
        file = open(classPath + "userdata\\characters.txt", "w")
        file.write(content)
        file.close()
        #'''
        #print("finished saving characters")
        
    def convertCharacterToSaveFormat(self, characterToConvert):
        #print("converting characters to line")
        result = characterToConvert.characterId + ","
        result += characterToConvert.name + ","
        result += characterToConvert.weapon.name + ","
        result += str(characterToConvert.level) + ","
        result += characterToConvert.characterClass + ","
        result += characterToConvert.colour + ","
        for i in list(characterToConvert.armour.keys()):
            # change to characterToConvert.armour[i].name
            if characterToConvert.armour[i] != None:
                result += f"{characterToConvert.armour[i].name},"
            else:
                result += f"{characterToConvert.armour[i]},"
        for i in list(characterToConvert.attributePointDistribution.keys()):
            result += f"{characterToConvert.attributePointDistribution[i]},"
        for i in characterToConvert.talents:
            result += f"{i},"
        for i in characterToConvert.startingBuffs:
            result += f"{i},"
        #print("finished converting characters to line")
        return result

    def generateattributePoints(self, c):
        #print(f"generating attribute points for {c.name} as {c.characterClass}")
        for i in list(c.attributePoints.keys()):
            c.attributePoints[i] = 10
        match (c.characterClass):
            case "Warrior":
                c.attributePoints["constitution"] += (c.level-1) * 2
                c.attributePoints["strength"] += (c.level-1) * 2
            case "Mage":
                c.attributePoints["wisdom"] += (c.level-1) * 2
                c.attributePoints["intelligence"] += (c.level-1) * 2
            case "Ranger":
                c.attributePoints["agility"] += (c.level-1) * 2
                c.attributePoints["dexterity"] += (c.level-1) * 2
            case "Rogue":
                c.attributePoints["dexterity"] += (c.level-1) * 2
                c.attributePoints["wisdom"] += (c.level-1) * 2
            case "Druid":
                c.attributePoints["strength"] += (c.level-1) * 2
                c.attributePoints["wisdom"] += (c.level-1) * 2
        #print(f"finished generating attribute points for {c.name}")

    def generateBaseStatPoints(self, c):
        #print(f"generating stat points for {c.name}")
        statKeyList = list(c.baseStatPoints.keys())
        attrKeyList = list(c.attributePoints.keys())
        for i in range(len(attrKeyList)):
            if statKeyList[i] in ["health", "mana"]:
                c.baseStatPoints[statKeyList[i]] = 100 + 20 * (c.attributePoints[attrKeyList[i]]-10) + 10 * c.attributePointDistribution[attrKeyList[i]] + c.bonusAttributePoints[attrKeyList[i]]
            else:
                c.baseStatPoints[statKeyList[i]] = 10 + 2 * (c.attributePoints[attrKeyList[i]]-10) + c.attributePointDistribution[attrKeyList[i]] + c.bonusAttributePoints[attrKeyList[i]]
        #print(f"finished generating stat points for {c.name}")

    def getArmourStatBonuses(self, c):
        for i in c.armour.values():
            if i != None:
                for x in c.statPoints:
                    if x in i.multipliers:
                        c.statPoints[x] += int(i.multipliers[x])
            
    def getArmourAttributeBonuses(self, c):
        for i in c.armour.values():
            if i != None:
                for x in c.bonusAttributePoints:
                    if x in i.multipliers:
                        c.bonusAttributePoints[x] += int(i.multipliers[x])
            
    def getArmourMultiplierBonuses(self, c):
        for i in c.armour.values():
            if i != None:
                for x in i.multipliers:
                    if x in c.extraMultipliers:
                        c.extraMultipliers[x] += i.multipliers[x]
                    else:
                        c.extraMultipliers.update({x : i.multipliers[x]})

    def getWeaponStatBonuses(self, c):
        for x in c.statPoints:
            if x in c.weapon.multipliers:
                c.statPoints[x] += int(c.weapon.multipliers[x])

    def getWeaponAttributeBonuses(self, c):
        for x in c.bonusAttributePoints:
            if x in c.weapon.multipliers:
                c.bonusAttributePoints[x] += int(c.weapon.multipliers[x])

    def getWeaponMultiplierBonuses(self, c):
        for x in c.weapon.multipliers:
            if x in c.extraMultipliers:
                c.extraMultipliers[x] += c.weapon.multipliers[x]
            else:
                c.extraMultipliers.update({x : c.weapon.multipliers[x]})

    def generateStatPoints(self, c):
        self.generateAttributePoints(c)
        for i in c.statPoints:
            c.statPoints[i] = 0
        self.getArmourStatBonuses(c)
        self.getWeaponStatBonuses(c)
        self.generateBaseStatPoints(c)
        self.generateFinalStatPoints(c)
        for x in c.extraMultipliers:
            c.extraMultipliers[x] = 0
        self.getArmourMultiplierBonuses(c)
        self.getWeaponMultiplierBonuses(c)
        self.getDefence(c)

    def generateAttributePoints(self, c):
        self.generateattributePoints(c)
        for i in c.bonusAttributePoints:
            c.bonusAttributePoints[i] = 0
        self.getArmourAttributeBonuses(c)
        self.getWeaponAttributeBonuses(c)
        self.generatePotionBonuses(c)
             
    def generatePotionBonuses(self, c):
        damagePotions = ["strength", "intelligence", "dexterity"]
        b = buffController()
        for i in damagePotions:
            if b.characterHasBuffName(c, f"{i} potion"):
                c.bonusAttributePoints[i] += int((c.attributePoints[i] + c.attributePointDistribution[i] + c.bonusAttributePoints[i]) * 0.3)

    def generateFinalStatPoints(self, c):
        for i in c.baseStatPoints:
            c.statPoints[i] += c.baseStatPoints[i]
        
        b = buffController()
        if b.characterHasBuffName(c, "enrage"):
            c.statPoints["melee damage"] = int(c.statPoints["melee damage"] * (1.2 + ((c.attributePoints["strength"] + c.attributePointDistribution["strength"] + c.bonusAttributePoints["strength"]) * 0.002)))
        
            
    def getMaximumAttributePoints(self, c):
        #print(f"generating maximum attribute points for {c.name}")
        return (c.level-1) * 3

    def addWeaponDmgToStatPoints(self, c):
        match (c.weapon.classRestriction):
            case "Warrior":
                c.statPoints["melee damage"] += c.weapon.baseDmg
            case "Mage":
                c.statPoints["magic damage"] += c.weapon.baseDmg
            case "Ranger":
                c.statPoints["ranged damage"] += c.weapon.baseDmg
            case "Rogue":
                c.statPoints["ranged damage"] += c.weapon.baseDmg
            case "Druid":
                c.statPoints["melee damage"] += c.weapon.baseDmg

    def getDefence(self, c):
        a = armourController()
        c.defence = a.getDefence(c)
        for x in c.weapon.multipliers:
            if x == "defence":
                c.defence += c.weapon.multipliers[x]

    def changeClass(self, c, characterClass):
        if characterClass != c.characterClass:
            print(f"changed class to {characterClass}")
            c.characterClass = characterClass
            a = armourController()
            for i in c.armour:
                if c.armour[i].classRestriction not in ["None", c.characterClass]:
                    print(f"Armour {c.armour[i]} removed as {c.armour[i].classRestriction}")
                    c.armour[i] = a.none()
            if c.weapon.classRestriction not in ["None", c.characterClass]:
                print(f"Armour {c.weapon} removed as {c.weapon.classRestriction}")
                w = weaponController()
                c.weapon = w.fist()
        











