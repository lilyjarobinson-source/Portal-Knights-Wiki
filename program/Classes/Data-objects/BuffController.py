class buff:
    def __init__(self):
        self.name = ""
        self.buffType = ""
        self.sharedCooldownName = ""
        self.activeTime = 0
        self.cooldown = 0
        # buffType in ["buff", "shout", "recoveryPotion", "buffPotion"]

    def toString(self):
        return f"Buff : {self.name}, {self.buffType}, {self.sharedCooldownName}, {self.activeTime}, {self.cooldown}"

    def getActiveTimer(self):
        return timer(self.name, self.activeTime)
    
    def getCooldownTimer(self, cooldownModifier=1):
        if self.sharedCooldownName == "":
            return timer(self.name, self.cooldown * cooldownModifier)
        return timer(self.buffType, self.cooldown * cooldownModifier)

class timer:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def updateAndCheck(self, deltaTime):
        self.time -= deltaTime
        return self.time < 0

    def toString(self):
        return f"Timer : {self.name}, {self.time}"

class buffController:
    def __init__(self):
        self.buffs = []
        self.buffsToApply = ["enrage", "war cry", "strength potion"]

    def loadBuffs(self):
        self.buffs = []
        
        classPath = __file__.split("program")[0]
        file = open(f"{classPath}program\\Recourses\\buffs.txt", "r")
        contents = file.read()
        file.close()

        contents = contents.split("\n")[:-1]

        for i in contents:
            self.buffs.append(self.getBuffFromData(i))

    def getBuffFromData(self, line):
        line = line.split(",")
        b = buff()
        b.name = line[0]
        b.buffType = line[1]
        b.sharedCooldownName = line[2]
        b.activeTime = int(line[3])
        b.cooldown = int(line[4])
        return b

    def updateBuffs(self, c, deltaTime):
        buffsToRemove = []
        for i in range(len(c.buffTimers)):
            if c.buffTimers[i].updateAndCheck(deltaTime):
                buffsToRemove.insert(0, i)
        cooldownsToRemove = []
        for i in range(len(c.cooldownTimers)):
            if c.cooldownTimers[i].updateAndCheck(deltaTime):
                cooldownsToRemove.insert(0, i)
        for i in buffsToRemove:
            c.buffTimers.pop(i)
        for i in cooldownsToRemove:
            c.cooldownTimers.pop(i)
    
    def checkToApplyBuffs(self, c):
        for i in self.buffs:
            if i.name in self.buffsToApply:
                isAlreadyThereAndShout = False
                if i.buffType == "shout":
                    for x in c.buffTimers:
                        if x.name == i.name:
                            isAlreadyThereAndShout = True
                if not isAlreadyThereAndShout and self.applyBuff(c, i):
                    return True
        return False

    def applyStartingBuffs(self, c):
        c.buffTimers = []
        c.cooldownTimers = []
        for i in c.startingBuffs:
            buffToApply = self.getBuff(i)
            cooldownModifier = self.getTalentCooldownModifier(c, buffToApply)
            c.buffTimers.append(buffToApply.getActiveTimer())
            c.cooldownTimers.append(buffToApply.getCooldownTimer(cooldownModifier))
    
    def applyStartingBuff(self, c, buffToApply):
        if buffToApply not in c.startingBuffs:
            c.startingBuffs.append(buffToApply)
            return True
        return False

    def applyBuff(self, c, buffToApply):
        if self.checkToApplyBuff(c, buffToApply):
            cooldownModifier = self.getTalentCooldownModifier(c, buffToApply)
            c.buffTimers.append(buffToApply.getActiveTimer())
            c.cooldownTimers.append(buffToApply.getCooldownTimer(cooldownModifier))
            return True
        return False

    def getTalentCooldownModifier(self, c, b):
        modifier = 1
        if b.buffType == "shout":
            if c.characterClass == "Warrior":
                if c.talents[3] == 0:
                    modifier = 0.75
        return modifier
        

    def applyBuffName(self, c, buffName):
        buffToApply = self.getBuff(buffName)
        return self.applyBuff(c, buffToApply)


    def checkToApplyBuff(self, c, b):
        if b.sharedCooldownName == "":
            for i in c.cooldownTimers:
                if b.name == i.name:
                    return False
        else:
            for i in c.cooldownTimers:
                if b.sharedCooldownName == i.name:
                    return False
        return True

    def getBuffIndex(self, name, buffList):
        for i in range(len(buffList)):
            if name == buffList[i].name:
                return i
        return -1

    def characterHasBuffName(self, c, buffName):
        for i in c.buffTimers:
            if buffName == i.name:
                return True
        return False
        
    def getBuff(self, name):
        for i in self.buffs:
            if name == i.name:
                return i
