import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from Character import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterTalentMenu(characterMenuTemplate):
    def initialise(self, root):
        self.loadCharacter()
        self.displayLevel()

    def displayLevel(self):
        self.icons["levelEntry"].set(self.loadedCharacter.level)
