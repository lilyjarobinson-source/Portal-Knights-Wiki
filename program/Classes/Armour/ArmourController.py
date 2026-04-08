from Armour import armour

class armourController:
    def loadArmourPieces():
        location = "ArmourPieces.txt"#"Classes\\Armour\\ArmourPieces.txt"
        armourPieces = []
        with open(location, "r") as file:
            contents = file.read()
            contents = contents.split("\n")
            for i in range(len(contents)-1):
                item = contents[i].split(",")
                a = armour()
                a.name = item[0]
                a.requiredLevel = int(item[1])
                a.baseDefence = int(item[2])
                a.classRestriction = item[3]
                a.slot = item[4]
                a.perk = item[5]
                a.multipliers = armourController.getMultipliers(item[6:-1])
                armourPieces.append(a)
        for i in armourPieces:
            print(i.toString())
        return armourPieces

    def getMultipliers(listOfMults):
        multipliers = {}
        for i in listOfMults:
            i = i.split("=")
            multipliers.update({i[0]:float(i[1])})
        return multipliers

armourController.loadArmourPieces()
