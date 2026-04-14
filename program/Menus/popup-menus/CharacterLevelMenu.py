import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from CharacterController import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterLevelMenu(characterMenuTemplate):
    def assignAttributePoints(self):
        pass

    def displayAvailibleAttributePoints(self):
        pass

    def displayAttributePoints(self):
        pass

    def resetAttributePoints(self):
        pass
