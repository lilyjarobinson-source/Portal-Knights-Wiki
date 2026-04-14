import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from CharacterController import character
from CharacterController import characterController
from Menu import menu

class characterMenuTemplate(menu):
    character = None
    characters = []
    classPath = __file__.split("Menus")[0]

    def loadCharacters(self):
        self.characters = characterController.getAllCharacters()

    def saveCharacter(self):
        characterController.saveCharacterData(self.character)

    def saveCharacters(self):
        characterController.saveCharacters(self.characters)

    def loadCharacter(self):
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "r")
        characterId = file.read()
        file.close()

        for i in self.characters:
            if i.characterId == characterId:
                self.character = i
                    
        
