import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from Character import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterArmourMenu(characterMenuTemplate):
    def initialise(self, root):
        self.loadCharacter()

    def displayArmour(self):
        pass

    def assignArmourToSlot(self, slot):
        pass

    
