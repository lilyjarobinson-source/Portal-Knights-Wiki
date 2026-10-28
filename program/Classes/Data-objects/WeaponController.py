from Weapon import weapon
class weaponController:
    weaponTypeDictionary = {
        "warrior" : {
            "sword" : [1, 3/10],
            "hammerl" : [7/3, 7/10],
            "hammers" : [4/3, 2/5],
            "axe" : [7/3, 7/10],
            "axes" : [1, 3/10],
            "saber" : [1, 3/10],
            "club" : [4/3, 2/5],
            "mace" : [4/3, 2/5],
            "knife" : [11/10, 8/25],
            "gauntlet" : [9/10, 1/4],
            "weapon" : [1, 2/5]
        },
        "ranger" : {
            "bow" : [1, 5/3],
            "crossbow" : [11/6, 3/10],
            "slingshot" : [4/3, 2/5],
            "dagger" : [9/10, 1/4],
            "gun" : [5/6, 7/10],
            "knife" : [4/3, 3/10],
            "weapon" : [1, 2/5]
        },
        "none" : {
            "saber" : [1, 3/10],
            "weapon" : [1, 2/5],
            "crossbow" : [11/6, 3/10],
            "bow" : [1, 5/3],
        },
        
    }

    def __init__(self):
        self.weapons = []

    def fist(self):
        fist = weapon()
        fist.name = "Fist"
        fist.classRestriction = "none"
        fist.requiredLevel = 0
        fist.wpnType = "weapon"
        fist.damageType = "melee damage"
        fist.damageStat = "physical"
        self.getWeaponDmgMultAndHitRate(fist)
        return fist

    def loadWeapons(self, c):
        self.weapons = []
        for i in ["Common", c.characterClass]:
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
        try:
            step = 0
            line = line.split(",")
            w = weapon()
            w.name = line[0]
            step += 1
            w.classRestriction = line[1]
            step += 1
            w.damageType = line[2]
            step += 1
            w.damageStat = line[3]
            step += 1
            w.requiredLevel = int(line[4])
            step += 1
            w.baseDmg = int(line[5])
            step += 1
            w.wpnType = line[6]
            step += 1
            w.multipliers = self.getMultipliers(line[7:-1])
            step += 1
            self.getWeaponDmgMultAndHitRate(w)
            step += 1
            return w
        except:
            print("Failed at line\n" + str(line) + "\nAt step:" + str(step))
            return self.fist()

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

            

