import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from ArmourController import armourController
from CharacterMenuTemplate import characterMenuTemplate

class characterArmourMenu(characterMenuTemplate):
    def __init__(self):
        self.armourController = armourController()
        self.displayArmourPieces = []
        self.searchingSlot = None
        
    def initialise(self, root):
        self.armourController.loadArmourPieces()
        self.loadCharacter()
        self.displayArmour()
        self.displayClass()
        self.searchForArmour("Ring")
        self.displayArmourOptions()

        self.icons["headEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Head"))
        self.icons["torsoEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Torso"))
        self.icons["armsEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Arms"))
        self.icons["legsEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Legs"))
        self.icons["capeEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Cape"))
        self.icons["ringEntry"].bindFunctionToKeypress(lambda : self.searchAndAssign("Ring"))



    def displayArmour(self):
        for i in self.armourController.armourSlots:
            if self.loadedCharacter.armour[i] != None:
                self.icons[f"{i.lower()}Entry"].set(self.loadedCharacter.armour[i].name)
            else:
                self.icons[f"{i.lower()}Entry"].set(self.loadedCharacter.armour[i])

    def displayClass(self):
        self.icons["classOptionBox"].setSelectedOption(self.loadedCharacter.characterClass)

    def setClass(self):
        self.loadedCharacter.characterClass = self.icons["classOptionBox"].get()
        self.saveCharacter()
        self.displayArmour()

    def assignArmourToSlot(self):
        if self.searchingSlot == None:
            return None
        value = self.icons["armourListBox"].getValue()
        armourPiece = self.armourController.getArmourPiece(value)
        if value == "None":
            self.icons[f"{self.searchingSlot.lower()}Entry"].set(armourPiece)
        elif value != None:
            self.icons[f"{self.searchingSlot.lower()}Entry"].set(armourPiece.name)
        else:
            value = self.icons[f"{self.searchingSlot.lower()}Entry"].get()
            armourPiece = self.armourController.getArmourPiece(value)
            
        self.loadedCharacter.armour[self.searchingSlot] = armourPiece
        if armourPiece != None:
            self.displayArmourStats(armourPiece)
        self.saveCharacter()

    def searchAndAssign(self, slot):
        self.searchForArmour(slot)
        self.assignArmourToSlot()

    def searchForArmour(self, slot):
        self.searchingSlot = slot
        self.displayArmourPieces = []
        containsString = self.icons[f"{slot.lower()}Entry"].get().lower()
        for i in self.armourController.armourPieces:
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

    def displayArmourStats(self, a):
        self.icons["nameLabel"].set(a.name)
        if a.buff == "":
            self.icons["buffLabel"].deactivate()
            self.icons["multiplierListBox"].place([1, 200], [199, 49])
        else:
            self.icons["buffLabel"].activate(self.root, self.theme, self.isPopupMenuClosedFunction)
            self.icons["buffLabel"].set(a.buff)
            self.icons["multiplierListBox"].place([1, 220], [199, 29])
        self.icons["multiplierListBox"].clear()
        for i in a.multipliers:
            self.icons["multiplierListBox"].append(f"{i} : {a.multipliers[i]}")
    
