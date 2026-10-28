from CharacterMenuTemplate import characterMenuTemplate

class characterOptionsMenu(characterMenuTemplate):
    def assignIconFunctions(self):
        self.icons["selectCharButton"].bindFunction(self.selectCharacter)
        self.icons["saveCharButton"].bindFunction(self.saveCharacter)
        self.icons["loadCharsButton"].bindFunction(self.refreshList)
        self.icons["newCharButton"].bindFunction(lambda : self.main.changeMenu("characterNewMenu"))
        self.icons["deleteCharButton"].bindFunction(self.deleteCharacter)
    
    def initialise(self):
        self.refreshList()

    def selectCharacter(self):
        index = self.icons["charactersListBox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "w")
        file.write(self.characterController.convertCharacterToSaveFormat(self.characters[index]))
        file.close()
        self.main.changeMenu("characterOverviewMenu")

    def displayCharacters(self):
        self.icons["charactersListBox"].clear()
        for i in self.characters:
            self.icons["charactersListBox"].append(f"{i.name} - {i.characterClass} - lvl:{i.level}")

    def refreshList(self):
        self.loadCharacters()
        self.displayCharacters()

    def deleteCharacter(self):
        index = self.icons["charactersListBox"].getIndex()
        if len(index) == 0:
            return None
        self.icons["charactersListBox"].delete(index[0])
        self.characters.pop(index[0])
        self.saveCharacters()
    
