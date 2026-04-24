import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from Character import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterNewMenu(characterMenuTemplate):
    def initialise(self, root):
        self.generateNewCharacter()
        
    def generateNewCharacter(self):
        self.loadedCharacter = self.characterController.new()

    def createCharacter(self, main):
        self.loadedCharacter.name = self.icons["nameEntry"].get()
        self.loadedCharacter.characterClass = self.icons["classOptionBox"].get()
        if self.loadedCharacter.name == "":
            print("No name")
            return None
        self.saveCharacter()
        main.changeMenu(0)
        
    
