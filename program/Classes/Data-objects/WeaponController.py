from Weapon import weapon
from WeaponType import *

class weaponController:
    weaponTypeDictionary = {
        "Warrior" : {
            "Sword" : [1, 3/10],
            "HammerL" : [7/3, 7/10],
            "HammerS" : [4/3, 2/5],
            "Axe" : [7/3, 7/10],
            "AxeS" : [1, 3/10],
            "Saber" : [1, 3/10],
            "Club" : [4/3, 2/5],
            "Mace" : [4/3, 2/5],
            "Knife" : [11/10, 8/25],
            "Gauntlet" : [9/10, 1/4],
            "Weapon" : [1, 2/5]
        },
        "None" : {
            "Saber" : [1, 3/10],
            "Weapon" : [1, 2/5]
        }
    }

    def __init__(self):
        self.weapons = []

    def loadWeapons(self):
        self.weapons = []
        for i in ["Common", "Warrior"]:
            contents = self.loadWeaponsFileContent(i)
            for line in contents:
                self.weapons.append(self.getWeaponDataFromLine(line))

    def loadWeaponsFileContent(self, name):
        classPath = __file__.split("program")[0]
        file = open(f"{classPath}program\\Recourses\\Weapons\\{name}.txt", "r")
        contents = file.read()
        file.close()
        return contents.split("\n")[:-1]

    def getWeaponDataFromLine(self, line):
        line = line.split(",")
        w = weapon()
        w.name = line[0]
        w.classRestriction = line[1]
        w.requiredLevel = int(line[2])
        w.baseDmg = int(line[3])
        w.wpnType = line[4]
        w.multipliers = self.getMultipliers(line[5:-1])
        self.getWeaponDmgMultAndHitRate(w)
        return w

    def getWeapon(self, name):
        for i in self.weapons:
            if i.name.lower() == name.lower():
                return i

    def getWeaponDmgMultAndHitRate(self, w):
        w.dmgMult = self.weaponTypeDictionary[w.classRestriction][w.wpnType][0]
        w.hitInterval = self.weaponTypeDictionary[w.classRestriction][w.wpnType][1]

    def getMultipliers(self, listOfMults):
        multipliers = {}
        for i in listOfMults:
            i = i.split("=")
            multipliers.update({i[0]:float(i[1])})
        return multipliers

            

