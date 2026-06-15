class buff:
    def __init__(self):
        self.name = ""
        self.activeTime = 0
        self.cooldown = 0
        self.hasCooldown = 0
        # buffType in ["buff", "shout", "recoveryPotion", "buffPotion"]
        self.buffType = ""

class buffController:
    def __init__(self):
        self.buffs = []

    def loadBuffs(self):
        self.buffs = [buff(), buff(), buff(), buff()]
        
        self.buffs[0].name = "weaken enemy"
        self.buffs[0].activeTime = 3
        self.buffs[0].hasCooldown = False
        self.buffs[0].buffType = "buff"
        
        self.buffs[1].name = "enrage"
        self.buffs[1].activeTime = 10
        self.buffs[1].cooldown = 10
        self.buffs[1].hasCooldown = True
        self.buffs[1].buffType = "shout"
        
        self.buffs[2].name = "war cry"
        self.buffs[2].activeTime = 10
        self.buffs[2].cooldown = 10
        self.buffs[2].hasCooldown = True
        self.buffs[2].buffType = "shout"
        
        self.buffs[3].name = "strength potion"
        self.buffs[3].activeTime = 9
        self.buffs[3].hasCooldown = False
        self.buffs[3].buffType = "buffPotion"

    def cleanBuffs(self, c, deltaTime):
        buffsToRemove = []
        for i in c.cooldownTimers:
            if c.cooldownTimers[i].cooldown > 0:
                c.cooldownTimers[i].cooldown -= deltaTime
            else:
                buffsToRemove.append(i)
        for i in buffsToRemove:
            c.cooldownTimers.remove(i)
        if c.warriorShoutOnCooldown:
            c.warriorShoutCooldown -= deltaTime
            if c.warriorShoutCooldown < 0:
                c.warriorShoutOnCooldown = False
        if c.buffPotionOnCooldown:
            c.buffPotionCooldown -= deltaTime
            if c.buffPotionCooldown < 0:
                c.buffPotionOnCooldown = False
        
        buffsToRemove = []
        for i in c.buffs:
            if i.activeTime < 0:
                buffsToRemove.append(i)
            else:
                i.activeTime -= deltaTime
        for i in buffsToRemove:
            c.buffs.remove(i)
            if i.hasCooldown:
                match i.buffType:
                    case "buff":
                        c.cooldownTimers.update(i)
                    case "shout":
                        c.warriorShoutOnCooldown = True
                        c.warriorShoutCooldown = 10
                    case "buffPotion":
                        c.buffPotionOnCooldown = True
                        c.buffPotionCooldown = 0#i.cooldown
    
    def checkToApplyBuffs(self, c):
        for i in self.buffs[1:]:
            match i.buffType:
                case "buff":
                    if i not in c.buffs and i not in c.cooldownTimers:
                        c.buffs.append(i)
                        return True
                case "shout":
                    if self.checkIfBuffNameInList(i.name, c.buffs) == -1 and not c.warriorShoutOnCooldown:
                        c.buffs.append(i)
                        return True
                case "buffPotion":
                    if self.checkIfBuffNameInList(i.name, c.buffs) == -1 and not c.buffPotionOnCooldown:
                        c.buffs.append(i)
                        return True
        return False

    def checkIfBuffNameInList(self, name, buffList):
        for i in range(len(buffList)):
            if name == buffList[i].name:
                return i
        return -1

    def getBuff(self, name):
        for i in self.buffs:
            if name == i.name:
                return i
