from Menu import menu
class mainMenu(menu):
    def assignIconFunctions(self):
        self.icons["dmgCalcMenuButton"].bindFunction(lambda : self.main.changeMenu("dmgCalcMenu"))
        self.icons["characterEditingMenusButton"].bindFunction(lambda : self.main.changeMenu("characterOptionsMenu"))
