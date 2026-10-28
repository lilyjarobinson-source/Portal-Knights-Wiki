from CharacterMenuTemplate import characterMenuTemplate

class characterOptionsMenu(characterMenuTemplate):
    def initialise(self, root):
        self.refreshList()

    def selectCharacter(self, main):
        index = self.icons["charactersListBox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        file = open(self.classPath + "Recourses\\loadedCharacter.txt", "w")
        file.write(self.characterController.convertCharacterToSaveFormat(self.characters[index]))
        file.close()
        main.changeMenu(3)

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
    
