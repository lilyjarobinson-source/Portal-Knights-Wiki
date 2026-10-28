from CharacterController import characterController
from Menu import menu

class characterMenuTemplate(menu):
    def __init__(self):
        super().__init__()
        self.characterController = characterController()
        self.loadedCharacter = None
        self.characters = []
        self.classPath = __file__.split("Menus")[0]

    def loadCharacters(self):
        #print("loading characters")
        self.characters = self.characterController.getAllCharacters()
        #print("finished loading characters")

    def saveCharacter(self):
        #print("saving character")
        self.characterController.saveCharacterData(self.loadedCharacter)
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "w")
        file.write(self.characterController.convertCharacterToSaveFormat(self.loadedCharacter))
        file.close()
        #print("finished saving character")

    def saveCharacters(self):
        #print("saving characters")
        self.characterController.saveCharacters(self.characters)
        #print("finished saving characters")

    def loadCharacter(self):
        #print("loading character")
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "r")
        contents = file.read()
        file.close()

        self.loadedCharacter = self.characterController.getCharacterDataFromSaveLine(contents)
        #print("finished loading character")

    def prettyPrintToIcon(self, iconName, value):
        self.icons[iconName].set(self.uppercaseFirstLetter(str(value)))
        
    def uppercaseFirstLetter(self, word):
        return word[0].upper() + word[1:]
