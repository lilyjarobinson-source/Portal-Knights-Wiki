from Armour import armour

class armourController:
    armourSlots = ["Head", "Torso", "Arms", "Legs", "Cape", "Ring"]
    def __init__(self):
        self.armourPieces = []
    
    def loadArmourPieces(self, c):
        self.armourPieces = []
        for i in self.armourSlots:
            contents = self.loadArmourFileContent(i)
            for line in contents:
                self.armourPieces.append(self.getArmourDataFromLine(line))

        for i in range(len(self.armourPieces)-1, 0, -1):
            if self.armourPieces[i].classRestriction != "None" and self.armourPieces[i].classRestriction != c.characterClass:
                self.armourPieces.pop(i)

    def loadArmourFileContent(self, slot):
        classPath = __file__.split("program")[0]
        file = open(f"{classPath}program\\Recourses\\Armour\\{slot}.txt", "r")
        contents = file.read()
        file.close()
        return contents.split("\n")[:-1]

    def getArmourDataFromLine(self, line):
        try:
            line = line.split(",")
            a = armour()
            a.name = line[0]
            a.requiredLevel = int(line[1])
            a.baseDefence = int(line[2])
            a.classRestriction = line[3]
            a.slot = line[4]
            a.buff = line[5]
            a.multipliers = armourController.getMultipliers(line[6:-1])
            return a
        except:
            print(f"failed getting armour data from line:\n{line}")
            return self.none()

    def getMultipliers(listOfMults):
        multipliers = {}
        for i in listOfMults:
            i = i.split("=")
            multipliers.update({i[0]:float(i[1])})
        return multipliers

    def getArmourPiece(self, name):
        if str(name) == "None":
            return self.none()
        for i in self.armourPieces:
            if i.name.lower() == name.lower():
                return i
        return self.none()

    def getDefence(self, c):
        total = 0
        for i in c.armour.values():
            total += i.baseDefence
        return total

    def none(self):
        a = armour()
        a.name = "None"
        a.classRestriction = "None"
        return a
