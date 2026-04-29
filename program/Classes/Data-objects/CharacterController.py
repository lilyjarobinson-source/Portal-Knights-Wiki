import sys, random
from WeaponController import weaponController
from ArmourController import armourController
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
        w.loadWeapons()
        c.weapon = w.getWeapon("Fist")
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
        w.loadWeapons()
        a.loadArmourPieces()
        
        #print("getting character data from line")
        line = line.split(",")[:-1]
        c = character()
        c.characterId = line[0]
        c.name = line[1]
        
        c.weapon = w.getWeapon(line[2])
        
        c.level = int(line[3])
        c.characterClass = line[4]
        c.colour = line[5]
        keyList = list(c.armour.keys())
        for i in range(len(keyList)):
            c.armour[keyList[i]] = a.getArmourPiece(line[6 + i])
        attrKeyList = list(c.attributePoints.keys())
        for i in range(6):
            c.attributePointDistribution[attrKeyList[i]] = int(line[12 + i])
        #print("finished getting character data from line")
        return c

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
                result += str(characterToConvert.armour[i].name) + ","
            else:
                result += str(characterToConvert.armour[i]) + ","
        for i in list(characterToConvert.attributePointDistribution.keys()):
            result += str(characterToConvert.attributePointDistribution[i]) + ","
        #print("finished converting characters to line")
        return result

    def generateAttributePoints(self, c):
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
                c.baseStatPoints[statKeyList[i]] = 100 + 20 * (c.attributePoints[attrKeyList[i]]-10) + 10 * c.attributePointDistribution[attrKeyList[i]]
            else:
                c.baseStatPoints[statKeyList[i]] = 10 + 2 * (c.attributePoints[attrKeyList[i]]-10) + c.attributePointDistribution[attrKeyList[i]] + c.bonusAttributePoints[attrKeyList[i]]
        #print(f"finished generating stat points for {c.name}")

    def getArmourBonusPoints(self, c):
        for x in c.armourMultipliers:
            c.armourMultipliers[x] = 0
        for i in c.armour.values():
            if i != None:
                for x in c.statPoints:
                    if x in i.multipliers:
                        c.statPoints[x] += int(i.multipliers[x])
                for x in c.bonusAttributePoints:
                    if x in i.multipliers:
                        c.bonusAttributePoints[x] += int(i.multipliers[x])
                for x in i.multipliers:
                    if x in characterController.multipliers:
                        if x in c.armourMultipliers:
                            c.armourMultipliers[x] += i.multipliers[x]
                        else:
                            c.armourMultipliers.update({x : i.multipliers[x]})

    def generateStatPoints(self, c):
        for i in c.statPoints:
            c.statPoints[i] = 0
        self.generateAttributePoints(c)
        for i in c.bonusAttributePoints:
            c.bonusAttributePoints[i] = 0
        self.getArmourBonusPoints(c)
        self.generateBaseStatPoints(c)
        for i in c.baseStatPoints:
            c.statPoints[i] += c.baseStatPoints[i]

    def getMaximumAttributePoints(self, c):
        #print(f"generating maximum attribute points for {c.name}")
        return (c.level-1) * 3
        











