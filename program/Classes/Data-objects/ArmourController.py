from Armour import armour

class armourController:
    armourSlots = ["Head", "Torso", "Arms", "Legs", "Cape", "Ring"]
    def __init__(self):
        self.armourPieces = []
    
    def loadArmourPieces(self):
        location = "Classes\\Data-objects\\ArmourPieces.txt"
        self.armourPieces = []
        for i in self.armourSlots:
            for x in ["Common", "Warrior"]:
                contents = self.loadArmourFileContent(i, x)
                for line in contents:
                    self.armourPieces.append(self.getWeaponDataFromLine(line))

    def loadArmourFileContent(self, slot, name):
        classPath = __file__.split("program")[0]
        file = open(f"{classPath}program\\Recourses\\Armour\\{slot}\\{name}.txt", "r")
        contents = file.read()
        file.close()
        return contents.split("\n")[:-1]

    def getWeaponDataFromLine(self, line):
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

    def getMultipliers(listOfMults):
        multipliers = {}
        for i in listOfMults:
            i = i.split("=")
            multipliers.update({i[0]:float(i[1])})
        return multipliers

    def getArmourPiece(self, name):
        if name == None:
            return name
        for i in self.armourPieces:
            if i.name.lower() == name.lower():
                return i

    def getDefence(self, c):
        total = 0
        for i in c.armour.value():
            if i != None:
                total += i.baseDefence
        return total
