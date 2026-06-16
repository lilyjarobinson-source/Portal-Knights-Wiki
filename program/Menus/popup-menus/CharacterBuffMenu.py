import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus")
from BuffController import buffController
from CharacterMenuTemplate import characterMenuTemplate

class characterBuffMenu(characterMenuTemplate):
    def __init__(self):
        self.buffController = buffController()

    def initialise(self, root):
        self.loadCharacter()
        self.buffController.loadBuffs()
        self.buffController.applyStartingBuffs(self.loadedCharacter)
        self.displaybuffs()
        self.displayCharacterBuffs()

    def displaybuffs(self):
        self.icons["buffListBox"].clear()
        for i in self.buffController.buffs:
            self.icons["buffListBox"].append(i.name)

    def displayCharacterBuffs(self):
        self.icons["selectedBuffListBox"].clear()
        for i in self.loadedCharacter.buffTimers:
            self.icons["selectedBuffListBox"].append(i.name)

    def addBuff(self):
        index = self.icons["buffListBox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        self.buffController.applyBuff(self.loadedCharacter, self.buffController.buffs[index])
        self.loadedCharacter.startingBuffs.append(self.buffController.buffs[index].name)
        self.displayCharacterBuffs()
        self.saveCharacter()

    def removeBuff(self):
        index = self.icons["selectedBuffListBox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        buff = self.buffController.getBuff(self.loadedCharacter.startingBuffs.pop(index))
        self.buffController.applyStartingBuffs(self.loadedCharacter)
        self.displayCharacterBuffs()
        self.saveCharacter()
