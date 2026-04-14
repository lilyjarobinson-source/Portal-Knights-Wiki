import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from CharacterController import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterNewMenu(characterMenuTemplate):
    def initialise(self, root):
        self.generateNewCharacter()
        
    def generateNewCharacter(self):
        self.character = characterController.new()

    def createCharacter(self, main):
        self.character.name = self.icons["nameEntry"].get()
        self.character.characterClass = self.icons["classOptionBox"].get()
        if self.character.name == "":
            print("No name")
            return None
        self.saveCharacter()
        main.changeMenu(0)
        
    
