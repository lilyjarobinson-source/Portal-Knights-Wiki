import sys, random
from WeaponController import weaponController
from ArmourController import armourController
from Character import character
class characterController:
    def new():
        c = character()
        c.level = 1
        characterController.generateCharacterId(c)
        w = weaponController()
        w.loadWeapons()
        c.weapon = w.getWeapon("Fist")
        return c

    def generateStatPoints(character):
        for i in list(character.attributePoint.keys()):
            character.attributePoint[i] = 10 + character.attributePointDistribution[i]
        match (character.characterClass.lower()):
            case "warrior":
                character.attributePoint["constitution"] += ((character.level-1) * 2)
                character.attributePoint["strength"] += ((character.level-1) * 2)
            case "mage":
                character.attributePoint["wisdom"] += ((character.level-1) * 2)
                character.attributePoint["intelligence"] += ((character.level-1) * 2)
            case "ranger":
                character.attributePoint["agility"] += ((character.level-1) * 2)
                character.attributePoint["dexterity"] += ((character.level-1) * 2)
            case "rogue":
                character.attributePoint["dexterity"] += ((character.level-1) * 2)
                character.attributePoint["wisdom"] += ((character.level-1) * 2)
            case "druid":
                character.attributePoint["strength"] += ((character.level-1) * 2)
                character.attributePoint["wisdom"] += ((character.level-1) * 2)
        statKeyList = list(character.statPoint.keys())
        attrKeyList = list(character.attributePoint.keys())
        for i in range(len(attrKeyList)):
            character.statPoint[statKeyList[i]] = 10 + 2 * (character.attributePoint[attrKeyList[i]]-10)
        

    def generateCharacterId(character):
        characters = characterController.getAllCharacters()
        newId = characterController.generateNewId()
        idIsTaken = True
        while idIsTaken:
            idIsTaken = False
            for i in characters:
                if i.characterId == newId:
                    idIsTaken = True
                    newId = characterController.generateNewId()
                    break
        character.characterId = newId

    def generateNewId():
        newId = ""
        for i in range(6):
            newId += str(random.randint(0, 9))
        return newId

    def getAllCharacters():
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
        contents = contents.split("\n")[:-1]
        characters = []
        for i in contents:
            characters.append(characterController.getCharacterDataFromSaveLine(i))
        return characters

    def getCharacterDataFromSaveLine(line):
        line = line.split(",")[:-1]
        c = character()
        c.characterId = line[0]
        c.name = line[1]
        
        w = weaponController()
        w.loadWeapons()
        c.weapon = w.getWeapon(line[2])
        
        c.level = int(line[3])
        c.characterClass = line[4]
        c.unspentAttributePoints = int(line[5])
        keyList = list(c.armour.keys())
        for i in range(len(keyList)):
            c.armour[keyList[i]] = line[6 + i]
        
        attrKeyList = list(character.attributePoint.keys())
        for i in range(6):
            c.attributePointDistribution[attrKeyList[i]] = int(line[12 + i])
        characterController.generateStatPoints(c)
        return c

    def saveCharacterData(character):
        characters = characterController.getAllCharacters()
        charFound = False
        for i in range(len(characters)):
            if character.characterId == characters[i].characterId:
                characters[i] = character
                charFound = True
                break
        if not charFound:
            characters.append(character)
        characterController.saveCharacters(characters)

    def saveCharacters(characters):
        classPath = __file__.split("program")[0]
        content = ""
        for i in characters:
            content += characterController.convertCharacterToSaveFormat(i) + "\n"
        file = open(classPath + "userdata\\characters.txt", "w")
        file.write(content)
        file.close()

        
    def convertCharacterToSaveFormat(character):
        content = character.characterId + ","
        content += character.name + ","
        content += character.weapon.name + ","
        content += str(character.level) + ","
        content += character.characterClass + ","
        content += str(character.unspentAttributePoints) + ","
        for i in list(character.armour.keys()):
            # change to character.armour[i].name
            content += str(character.armour[i]) + ","
        for i in list(character.attributePointDistribution.keys()):
            content += str(character.attributePointDistribution[i]) + ","
        return content
        












