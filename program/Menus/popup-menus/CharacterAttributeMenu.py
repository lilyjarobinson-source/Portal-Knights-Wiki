import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from CharacterMenuTemplate import characterMenuTemplate

class characterAttributeMenu(characterMenuTemplate):
    def initialise(self, root):
        self.loadCharacter()
        for i in ["constitution", "strength", "agility", "dexterity", "intelligence", "wisdom"]:
            self.icons[f"{i}AssignedPointsEntry"].set(self.loadedCharacter.attributePointDistribution[i])

        self.icons[f"constitutionAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("constitution"))
        self.icons[f"strengthAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("strength"))
        self.icons[f"agilityAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("agility"))
        self.icons[f"dexterityAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("dexterity"))
        self.icons[f"intelligenceAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("intelligence"))
        self.icons[f"wisdomAssignedPointsEntry"].bindFunctionToKeypress(lambda *args : self.assignAttributePoints("wisdom"))

        self.icons["levelEntry"].bindFunctionToKeypress(lambda *args : self.setLevel())


        self.displayLevel()
        self.displayAttributePoints()
        self.displayStatPoints()
        self.displayClass()
        print()
        for i in self.icons.keys():
            try:
                print(i, self.icons[i].get())
                print(f"object - {i}", self.icons[i].obj.get())
            except:pass
        
    def assignAttributePoints(self, key):
        amount = self.icons[f"{key}AssignedPointsEntry"].get()
        if amount == "":
            self.icons[f"{key}AssignedPointsEntry"].set("0")
        else:
            try:
                amount = int(amount)
            except:
                return None
            if amount < 0:
                self.loadedCharacter.attributePointDistribution.update({key : 0})
                self.icons[f"{key}AssignedPointsEntry"].set(0)

            else:
                self.loadedCharacter.attributePointDistribution.update({key : amount})
                remainingPoints = self.characterController.getMaximumStatPoints(self.loadedCharacter) - self.getTotalAssignedPoints()
                if remainingPoints < 0:
                    self.loadedCharacter.attributePointDistribution.update({key : amount + remainingPoints})
                    self.icons[f"{key}AssignedPointsEntry"].set(self.loadedCharacter.attributePointDistribution[key])
            self.displayAttributePoints()
            self.displayStatPoints()
            self.saveCharacter()
                    

    def getTotalAssignedPoints(self):
        total = 0
        for i in self.loadedCharacter.attributePointDistribution.values():
            total += i
        return total
    
    def displayLevel(self):
        self.icons["levelEntry"].set(self.loadedCharacter.level)

    def setLevel(self):
        amount = self.icons["levelEntry"].get()
        if amount == "":
            self.icons["levelEntry"].set("1")
        else:
            try:
                amount = int(amount)
            except:
                return None
            if amount < self.loadedCharacter.level:
                self.resetAttributePoints()
            if amount < 1:
                self.loadedCharacter.level = 1
                self.icons["levelEntry"].set(1)
            else:
                self.loadedCharacter.level = amount
                remainingPoints = 30 - amount
                if remainingPoints < 0:
                    self.loadedCharacter.level = amount + remainingPoints
                    self.icons["levelEntry"].set(self.loadedCharacter.level)
            self.displayLevel()
            self.displayAttributePoints()
            self.displayStatPoints()
            self.saveCharacter()

    def displayAvailibleAttributePoints(self):
        pass

    def displayAttributePoints(self):
        print("displaying attribute points")
        self.characterController.generateAttributePoints(self.loadedCharacter)
        for i in ["constitution", "strength", "agility", "dexterity", "intelligence", "wisdom"]:
            self.icons[f"{i}BaseLabel"].set(self.loadedCharacter.attributePoints[i])
            self.icons[f"{i}AssignedPointsEntry"].set(self.loadedCharacter.attributePointDistribution[i])
            self.icons[f"{i}TotalLabel"].set(self.loadedCharacter.attributePoints[i] + self.loadedCharacter.attributePointDistribution[i])
        
    def displayStatPoints(self):
        print("displaying stat points")
        self.characterController.generateStatPoints(self.loadedCharacter)
        for i in ["health", "melee damage", "movement speed", "ranged damage", "magic damage", "mana"]:
            self.icons[f"{i}BaseLabel"].set(self.loadedCharacter.statPoints[i])
            self.icons[f"{i}TotalLabel"].set(self.loadedCharacter.statPoints[i])
    
    def resetAttributePoints(self):
        print("reseting attribute points")
        for i in ["constitution", "strength", "agility", "dexterity", "intelligence", "wisdom"]:
            self.loadedCharacter.attributePointDistribution.update({i : 0})
        self.displayAttributePoints()
        self.displayStatPoints()

    def displayClass(self):
        print("displaying class")
        self.icons["classOptionBox"].setSelectedOption(self.loadedCharacter.characterClass)

    def setClass(self):
        pass
        
