import sys
sys.path.append(__file__.split("Menus")[0] + "Menus")
from CharacterMenuTemplate import characterMenuTemplate

class canvasTextBox:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.drawPoint = [0,0]

    def display(self, canvas):
        canvas.write(
            self.drawPoint[0], self.drawPoint[1],
            self.name,
            "nw",
            "TkFixedFont"
        )
    

class dataValue(canvasTextBox):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.value = ""
        self.type = ""

    def formatText(self):
        self.text = f"{self.name} : "
        match (self.type):
            case "integer":
                self.value = int(float(self.value))
            case "percent":
                self.value = f"{int(float(self.value))}%"
            case "multiplier":
                self.value = f"x{self.value}"

    def display(self, canvas):
        canvas.write(
            self.drawPoint[0], self.drawPoint[1],
            f"{self.name} : {self.value}",
            "nw",
            "TkFixedFont"
        )

class camera:
    def __init__(self):
        self.position = [0,0]
        self.zoomScale = 1

    def translate(self, vector):
        self.position[0] += vector[0]
        self.position[1] += vector[1]

    def seeDataValue(self, dataValue):
        dataValue.drawPoint = [(-dataValue.position[0] - self.position[0]) / self.zoomScale, (dataValue.position[1] - self.position[1]) / self.zoomScale]

class characterOverviewMenu(characterMenuTemplate):
    def __init__(self):
        self.camera = None
        self.oldMousePos = [0, 0]
        self.multipliers = {}
        self.offensiveMultipliers = {}
        self.defensiveMultipliers = {}
        self.miscellaneousMultipliers = {}
        self.loadMultiplierTypes()
    
    def initialise(self, root):
        self.dataValues = {
            "characterName" : dataValue("Name ", [0, 0]),
            "characterLevel" : dataValue("Level", [0, 15]),
            "characterClass" : dataValue("Class", [0, 30]),

            "weapon" : canvasTextBox("Weapon", [-200, 15]),
            "weaponName" : canvasTextBox("", [-200, 30]),

            "stats" : canvasTextBox("Stats", [0, 60]),

            "armour" : canvasTextBox("Armour", [-200, 60]),

            "offensiveMultipliers" : canvasTextBox("Offensive multipliers", [0, 180]),
            "defensiveMultipliers" : canvasTextBox("", [-250, 180]),
            "miscellaneousMultipliers" : canvasTextBox("", [-500, 180]),
        }
        
        self.icons["canvas"].obj.bind('<ButtonPress-2>', lambda event : self.resetCamera())
        self.icons["canvas"].obj.bind('<ButtonPress-3>', self.dragCanvasStart)
        self.icons["canvas"].obj.bind('<B3-Motion>', lambda event : self.drag(event))
        if self.camera == None:
            self.camera = camera()
        self.resetCamera()
        self.loadCharacter()
        self.characterController.generateStatPoints(self.loadedCharacter)
        self.setupValues()
        self.updateCanvas()

    def updateCanvas(self):
        self.icons["canvas"].clear()
        for i in self.dataValues:
            self.camera.seeDataValue(self.dataValues[i])
            self.dataValues[i].display(self.icons["canvas"])

    def resetCamera(self):
        self.camera.position = [-2, 0]
        self.updateCanvas()
    
    def dragCanvasStart(self, event):
        self.oldMousePos = [event.x, event.y]
            
    def drag(self, event):
        mousePos = [event.x, event.y]
        self.camera.translate([(self.oldMousePos[0] - mousePos[0]) * self.camera.zoomScale, (self.oldMousePos[1] - mousePos[1]) * self.camera.zoomScale])
        self.oldMousePos = mousePos.copy()
        self.updateCanvas()

    def drawDictionaryFrom(self, iconName, dictionary):
        keyList = list(dictionary.keys())
        datumLabelPosition = self.dataValues[iconName].position.copy()
        
        maximumLength = 0
        nameAdditionalSpaces = {}
        valueAdditionalSpaces = {}
        for i in keyList:
            length = len(i)
            if length > maximumLength:
                maximumLength = length
        for i in keyList:
            length = len(i)
            nameAdditionalSpaces.update({i : " " * (maximumLength - length)})
        maximumLength = 0
        for i in keyList:
            length = len(f"{dictionary[i]}")
            if length > maximumLength:
                maximumLength = length
        for i in keyList:
            length = len(f"{dictionary[i]}")
            valueAdditionalSpaces.update({i : " " * (maximumLength - length)})
        
        for i in range(len(keyList)):
            self.dataValues.update({f"{iconName}{keyList[i]}" : dataValue(self.uppercaseFirstLetter(keyList[i]) + nameAdditionalSpaces[keyList[i]], [datumLabelPosition[0], datumLabelPosition[1] + 15 * (i+1)])})
            self.dataValues[f"{iconName}{keyList[i]}"].value = f"{valueAdditionalSpaces[keyList[i]]}{dictionary[keyList[i]]}"

    def drawMultipliersDictionary(self, iconName, dictionary, typeDictionary):
        keyList = list(dictionary.keys())
        datumLabelPosition = self.dataValues[iconName].position.copy()
        maximumLength = 0
        nameAdditionalSpaces = {}
        valueAdditionalSpaces = {}
        for i in keyList:
            length = len(i)
            if length > maximumLength:
                maximumLength = length
        for i in keyList:
            length = len(i)
            nameAdditionalSpaces.update({i : " " * (maximumLength - length)})
        
        for i in range(len(keyList)):
            self.dataValues.update({f"{iconName}{keyList[i]}" : dataValue(self.uppercaseFirstLetter(keyList[i]) + nameAdditionalSpaces[keyList[i]], [datumLabelPosition[0], datumLabelPosition[1] + 15 * (i+1)])})
            self.dataValues[f"{iconName}{keyList[i]}"].type = typeDictionary[keyList[i].lower()]
            self.dataValues[f"{iconName}{keyList[i]}"].value = dictionary[keyList[i]]
            self.dataValues[f"{iconName}{keyList[i]}"].formatText()
        
        maximumLength = 0
        for i in keyList:
            length = len(f"{self.dataValues[f"{iconName}{i}"].value}")
            if length > maximumLength:
                maximumLength = length
        for i in keyList:
            length = len(f"{self.dataValues[f"{iconName}{i}"].value}")
            valueAdditionalSpaces.update({i : " " * (maximumLength - length)})
        
        for i in range(len(keyList)):
            self.dataValues[f"{iconName}{keyList[i]}"].value = f"{valueAdditionalSpaces[keyList[i]]}{self.dataValues[f'{iconName}{keyList[i]}'].value}"


    def loadMultiplierTypes(self):
        self.loadMultiplierFile("offensive", self.offensiveMultipliers)
        self.loadMultiplierFile("defensive", self.defensiveMultipliers)
        self.loadMultiplierFile("miscellaneous", self.miscellaneousMultipliers)

    def loadMultiplierFile(self, name, dictionary):
        classPath = __file__.split("Menus")[0]
        file = open(f"{classPath}Recourses\\{name} multipliers.txt", "r")
        contents = file.read()
        contents = contents.split("\n")[:-1]
        file.close()
        for i in contents:
            i = i.split(",")[:-1]
            dictionary.update({i[0] : i[1]})
        

    def setupValues(self):
        self.dataValues["characterName"].value = self.loadedCharacter.name
        self.dataValues["characterLevel"].value = self.loadedCharacter.level
        self.dataValues["characterClass"].value = self.loadedCharacter.characterClass

        self.dataValues["weaponName"].name = self.loadedCharacter.weapon.name

        self.setUpStatPoints()
        self.setUpArmour()
        self.setUpMultipliers()

    def setUpStatPoints(self):
        self.drawDictionaryFrom("stats", self.loadedCharacter.statPoints)

    def setUpArmour(self):
        armour = {}
        for i in self.loadedCharacter.armour:
            armour.update({i : self.loadedCharacter.armour[i].name})
        self.drawDictionaryFrom("armour", armour)

    def setUpMultipliers(self):
        self.resetMultipliers()
        defaultEmptyMultipliers = {
            "Crit damage" : 1,
            "Multistrike rate" : 0,
            "Multistrike amount" : 1,
        }
        
        for i in self.loadedCharacter.extraMultipliers:
            if i in self.multipliers:
                self.multipliers[i] += self.loadedCharacter.extraMultipliers[i]
            else:
                self.multipliers.update({i : self.loadedCharacter.extraMultipliers[i]})

        for i in defaultEmptyMultipliers:
            if self.multipliers[i] == defaultEmptyMultipliers[i]:
                self.multipliers.pop(i)

        offensiveMultipliers = {}
        defensiveMultipliers = {}
        miscellaneousMultipliers = {}
        for i in self.multipliers:
            match (self.sortMultiplier(i)):
                case 1:
                    offensiveMultipliers.update({i : self.multipliers[i]})
                case 0:
                    miscellaneousMultipliers.update({i : self.multipliers[i]})
                case -1:
                    defensiveMultipliers.update({i : self.multipliers[i]})

        if len(defensiveMultipliers) == 0:
            self.dataValues["defensiveMultipliers"].name = ""
        else:
            self.dataValues["defensiveMultipliers"].name = "Defensive multipliers"
        if len(miscellaneousMultipliers) == 0:
            self.dataValues["miscellaneousMultipliers"].name = ""
        else:
            self.dataValues["miscellaneousMultipliers"].name = "Miscellaneous multipliers"
        
        
        self.drawMultipliersDictionary("offensiveMultipliers", offensiveMultipliers, self.offensiveMultipliers)
        self.drawMultipliersDictionary("defensiveMultipliers", defensiveMultipliers, self.defensiveMultipliers)
        self.drawMultipliersDictionary("miscellaneousMultipliers", miscellaneousMultipliers, self.miscellaneousMultipliers)

    def sortMultiplier(self, name):
        name = name.lower()
        if name in self.offensiveMultipliers:
            return 1
        if name in self.defensiveMultipliers:
            return -1
        if name in self.miscellaneousMultipliers:
            return 0
        return 0

    def resetMultipliers(self):
        self.multipliers = {
            "Crit rate" : 20,
            "Crit damage" : 1,
            "Multistrike rate" : 0,
            "Multistrike amount" : 1,
            "backstab" : 1.25,
        }

    def uppercaseFirstLetter(self, word):
        return word[0].upper() + word[1:]
