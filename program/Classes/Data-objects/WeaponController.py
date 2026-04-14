from Weapon import weapon
from WeaponType import *

class weaponController:
    weapons = []
    def loadWeapons(self):
        location = "Classes\\Data-objects\\Weapons.txt"
        self.weapons = []
        with open(location, "r") as file:
            contents = file.read()
            contents = contents.split("\n")
            for i in range(len(contents)-1):
                item = contents[i].split(",")
                w = weapon()
                w.name = item[0]
                w.requiredLevel = int(item[1])
                w.baseDmg = int(item[2])
                w.wpnType = self.setWeaponType(item[3])
                w.multipliers = self.getMultipliers(item[4:-1])
                self.weapons.append(w)

    def getWeapon(self, name):
        for i in self.weapons:
            if i.name.lower() == name.lower():
                return i

    def getWeapons(self):
        return self.weapons

    def setWeaponType(self, typeAsString):
        match typeAsString:
            case "Sword":
                return Sword()
            case "HammerL":
                return HammerL()
            case "HammerS":
                return HammerS()
            case "Axe":
                return Axe()
            case "AxeS":
                return AxeS()
            case "Saber":
                return Saber()
            case "Club":
                return Club()
            case "Mace":
                return Mace()
            case "Knife":
                return Knife()
            case "Gauntlet":
                return Gauntlet()
            case "Weapon":
                return Weapon()

    def getMultipliers(self, listOfMults):
        multipliers = {}
        for i in listOfMults:
            i = i.split("=")
            multipliers.update({i[0]:float(i[1])})
        return multipliers
            

