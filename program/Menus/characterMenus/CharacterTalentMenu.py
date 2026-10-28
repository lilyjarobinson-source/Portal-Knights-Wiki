from CharacterMenuTemplate import characterMenuTemplate

class characterTalentMenu(characterMenuTemplate):
    talents = {
        "warrior" : [
            ["Axe expert", "Hammer expert", "Sword expert"],
            ["Eye for an eye", "Fortification", "Commander"],
            ["Adrenaline Rush", "Last stand"],
            ["Aggression", "Determination"],
            ["Chain attacks", "Echo"],
            ["Finishing blow", "Tank mode", "Empowered Lung"],
            ["Combo swing", "Hardened armour", "Eternal rage"]
        ],
        "ranger" : [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ],
        "mage" : [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ],
        "rogue" : [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ],
        "druid" : [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ],
    }
    
    def initialise(self, root):
        self.icons["talent0OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(0))
        self.icons["talent1OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(1))
        self.icons["talent2OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(2))
        self.icons["talent3OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(3))
        self.icons["talent4OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(4))
        self.icons["talent5OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(5))
        self.icons["talent6OptionBox"].bindFunctionToKeypress(lambda *args : self.setTalent(6))

        
        self.icons["classOptionBox"].bindFunctionToKeypress(lambda *args : self.setClass())
        self.loadCharacter()
        self.displayLevel()
        self.setTalentOptions()

    def displayLevel(self):
        self.icons["levelEntry"].set(self.loadedCharacter.level)
        
    def setLevel(self):
        amount = self.icons["levelEntry"].get()
        if amount == "":
            self.icons["levelEntry"].set("1")
        else:
            try:
                amount = int(amount)
            except:
                return None
            if amount < 1:
                self.loadedCharacter.level = 1
                self.icons["levelEntry"].set(1)
            else:
                self.loadedCharacter.level = amount
                remainingPoints = 30 - amount
                if remainingPoints < 0:
                    self.loadedCharacter.level = amount + remainingPoints
                    self.icons["levelEntry"].set(self.loadedCharacter.level)
            self.displayLevel()
            self.saveCharacter()

    def displayClass(self):
        self.icons["classOptionBox"].setSelectedOption(self.loadedCharacter.characterClass)

    def setClass(self):
        self.characterController.changeClass(self.loadedCharacter, self.icons["classOptionBox"].get())
        self.saveCharacter()

    def setTalentOptions(self):
        for i in range(7):
            self.icons[f"talent{i}OptionBox"].setOptions(self.root, self.theme, self.talents[self.loadedCharacter.characterClass][i])
        self.displayTalents()

    def displayTalents(self):
        for i in range(7):
            self.icons[f"talent{i}OptionBox"].setSelectedOption(self.talents[self.loadedCharacter.characterClass][i][self.loadedCharacter.talents[i]])

    def setTalent(self, index):
        value = self.icons[f"talent{index}OptionBox"].get()
        self.loadedCharacter.talents[index] = self.talents[self.loadedCharacter.characterClass][index].index(value)
        self.saveCharacter()
