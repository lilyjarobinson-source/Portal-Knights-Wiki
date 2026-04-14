import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus\\framework")
from CharacterController import character
from CharacterController import characterController
from CharacterMenuTemplate import characterMenuTemplate

class characterOptionsMenu(characterMenuTemplate):
    def initialise(self, root):
        self.refreshList()

    def selectCharacter(self):
        index = self.icons["charactersListbox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "w")
        file.write(self.characters[index].characterId)
        file.close()

    def displayCharacters(self):
        self.icons["charactersListbox"].clear()
        for i in self.characters:
            self.icons["charactersListbox"].append(f"{i.name} - {i.characterClass} - lvl:{i.level}")

    def refreshList(self):
        self.loadCharacters()
        self.displayCharacters()

    def deleteCharacter(self):
        index = self.icons["charactersListbox"].getIndex()
        if len(index) == 0:
            return None
        self.icons["charactersListbox"].delete(index[0])
        self.characters.pop(index[0])
        self.saveCharacters()
    
