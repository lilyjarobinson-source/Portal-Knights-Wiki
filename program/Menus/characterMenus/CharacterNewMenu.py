from CharacterMenuTemplate import characterMenuTemplate

class characterNewMenu(characterMenuTemplate):
    def assignIconFunctions(self):
        self.icons["createCharacterButton"].bindFunction(self.createCharacter)
        self.icons["backButton"].bindFunction(lambda : self.main.changeMenu("characterOptionsMenu"))
        
    def initialise(self):
        self.generateNewCharacter()
        
    def generateNewCharacter(self):
        self.loadedCharacter = self.characterController.new()

    def createCharacter(self):
        self.loadedCharacter.name = self.icons["nameEntry"].get()
        self.loadedCharacter.characterClass = self.icons["classOptionBox"].get()
        if len(self.loadedCharacter.name) > 0:
            self.saveCharacter()
            self.main.changeMenu("characterOverviewMenu")
        else:
            print("No name")
        
    
