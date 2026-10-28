import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Menus")
from CharacterMenuTemplate import characterMenuTemplate

class characterNewMenu(characterMenuTemplate):
    def initialise(self, root):
        self.generateNewCharacter()
        
    def generateNewCharacter(self):
        self.loadedCharacter = self.characterController.new()

    def createCharacter(self, main):
        self.loadedCharacter.name = self.icons["nameEntry"].get()
        self.loadedCharacter.characterClass = self.icons["classOptionBox"].get()
        if len(self.loadedCharacter.name) > 0:
            self.saveCharacter()
            main.changeMenu(3)
        else:
            print("No name")
        
    
