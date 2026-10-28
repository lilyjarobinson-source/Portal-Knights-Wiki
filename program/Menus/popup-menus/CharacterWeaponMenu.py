import sys
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Menus")
from WeaponController import weaponController
from CharacterMenuTemplate import characterMenuTemplate

class characterWeaponMenu(characterMenuTemplate):
    def __init__(self):
        self.weaponController = weaponController()
        self.loadedWeapon = None
        
    def initialise(self, root):
        self.icons["classOptionBox"].bindFunctionToKeypress(lambda *args : self.setClass())
        
        self.loadCharacter()
        self.weaponController.loadWeapons(self.loadedCharacter)

        self.displayWeapons()
        self.loadCharacterWeapon()
        
        self.displayClass()
        self.displayWeapon()

    def displayWeapons(self):
        self.icons["weaponListBox"].clear()
        for i in self.weaponController.weapons:
            self.icons["weaponListBox"].append(i.name)

    def loadCharacterWeapon(self):
        self.loadedWeapon = self.loadedCharacter.weapon

    def setCharacterWeapon(self):
        value = self.icons["weaponListBox"].getValue()
        if None == 0:
            return None
        self.loadedWeapon = self.weaponController.getWeapon(value)
        self.loadedCharacter.weapon = self.loadedWeapon
        self.displayWeapon()
        self.saveCharacter()

    def displayClass(self):
        self.icons["classOptionBox"].setSelectedOption(self.loadedCharacter.characterClass)

    def setClass(self):
        self.characterController.changeClass(self.loadedCharacter, self.icons["classOptionBox"].get())
        self.saveCharacter()
        self.weaponController.loadWeapons(self.loadedCharacter)
        self.displayWeapons()

    def displayWeapon(self):
        self.icons["nameLabel"].set(self.loadedWeapon.name)
        self.prettyPrintToIcon("weaponTypeLabel", self.loadedWeapon.wpnType)
        self.prettyPrintToIcon("damageDisplayLabel", self.loadedWeapon.baseDmg)
        self.prettyPrintToIcon("dmgTypeLabel", self.loadedWeapon.damageType)
        self.icons["statListBox"].clear()
        for i in self.loadedWeapon.multipliers:
            if i != "defence":
                self.icons["statListBox"].append(f"{self.uppercaseFirstLetter(i)} : {self.loadedWeapon.multipliers[i]}")

        if "defence" in self.loadedWeapon.multipliers:
            self.icons["defenceDisplayLabel"].set(int(self.loadedWeapon.multipliers["defence"]))
        else:
            self.icons["defenceDisplayLabel"].set(0)
        
        if self.loadedWeapon.buff == "":
            self.icons["buffLabel"].deactivate()
            self.icons["statListBox"].place([1, 100], [199, 59])
        else:
            self.icons["buffLabel"].activate(self.root, self.theme, self.isPopupMenuClosedFunction)
            self.icons["statListBox"].place([1, 120], [199, 39])

    def getFilters(self):
        pass

    def resetFilters(self):
        pass

    def removeFilter(self):
        pass
    

    
