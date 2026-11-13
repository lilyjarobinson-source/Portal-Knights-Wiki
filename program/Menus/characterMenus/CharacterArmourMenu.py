from CharacterMenuTemplate import characterMenuTemplate

class characterArmourMenu(characterMenuTemplate):
    def __init__(self):
        super().__init__()
        self.displayArmourPieces = []
        self.searchingSlot = None

    def assignIconFunctions(self):
        self.icons["armourListBox"].bindFunctionToChange(self.assignArmourToSlot)
        
        self.icons["headEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("head"))
        self.icons["torsoEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("torso"))
        self.icons["armsEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("arms"))
        self.icons["legsEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("legs"))
        self.icons["capeEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("cape"))
        self.icons["ringEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("ring"))
        self.icons["classOptionBox"].bindFunctionToChange(self.setClass)
        
    def initialise(self):
        self.loadCharacter()
        self.displayArmour()
        self.displayClass()
        self.searchForArmour("head")
        self.displayArmourOptions()
        self.displayDefence()

    def displayArmour(self):
        for i in self.main.armourController.armourSlots:
            self.icons[f"{i.lower()}Entry"].set(self.loadedCharacter.armour[i].name)

    def displayClass(self):
        self.icons["classOptionBox"].setSelectedOption(self.loadedCharacter.characterClass)

    def displayDefence(self):
        self.main.characterController.getDefence(self.loadedCharacter)
        self.icons["defenceDisplayLabel"].set(self.loadedCharacter.defence)

    def setClass(self):
        self.main.characterController.changeClass(self.loadedCharacter, self.icons["classOptionBox"].get())
        self.saveCharacter()
        self.displayArmour()
        self.displayArmourOptions()

    def assignArmourToSlot(self):
        if self.searchingSlot == None:
            return ArmourController.none()
        value = self.icons["armourListBox"].getValue()
        armourPiece = self.main.armourController.getArmourPiece(value)
        if value == "None":
            self.icons[f"{self.searchingSlot.lower()}Entry"].set(armourPiece)
        elif value != None:
            self.icons[f"{self.searchingSlot.lower()}Entry"].set(armourPiece.name)
        else:
            value = self.icons[f"{self.searchingSlot.lower()}Entry"].get()
            armourPiece = self.main.armourController.getArmourPiece(value)
            
        self.loadedCharacter.armour[self.searchingSlot] = armourPiece
        self.displayArmourStats(armourPiece)
        self.saveCharacter()
        self.displayDefence()

    def searchAndAssign(self, slot):
        self.searchForArmour(slot)
        self.assignArmourToSlot()

    def searchForArmour(self, slot):
        self.searchingSlot = slot
        self.displayArmourPieces = []
        containsString = self.icons[f"{slot.lower()}Entry"].get().lower()
        for i in self.main.armourController.armourPieces:
            if i.slot == slot:
                if containsString in [None, "none", ""]:
                    self.displayArmourPieces.append(i)
                elif containsString in i.name.lower():
                    self.displayArmourPieces.append(i)
        self.displayArmourOptions()

    def displayArmourOptions(self):
        self.icons[f"armourListBox"].clear()
        for i in self.displayArmourPieces:
            self.icons[f"armourListBox"].append(i.name)
        self.icons["armourListCount"].set(len(self.displayArmourPieces))

    def displayArmourStats(self, a):
        self.icons["nameLabel"].set(a.name)
        if a.buff == "":
            self.icons["buffLabel"].deactivate()
            self.icons["multiplierListBox"].place([1, 201], [201, 59])
        else:
            self.icons["buffLabel"].activate(self.root, self.theme)
            self.icons["buffLabel"].set(a.buff)
            self.icons["multiplierListBox"].place([1, 221], [201, 39])
        self.icons["multiplierListBox"].clear()
        for i in a.multipliers:
            self.icons["multiplierListBox"].append(f"{i} : {a.multipliers[i]}")
    
