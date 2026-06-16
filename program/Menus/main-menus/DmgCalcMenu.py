import sys, time
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Classes\\Simulation")
sys.path.append(classPath + "Classes\\Graphing")
sys.path.append(classPath + "Menus")
from DamageCalculator import damageCalculator
from DamageStats import damageStats
from WeaponController import weaponController
from CharacterController import characterController
from BuffController import buffController
from PointCollection import pointCollection
from ScrollingGraph import scrollingGraph
from CharacterMenuTemplate import characterMenuTemplate

class dmgCalcMenu(characterMenuTemplate):
    characterController = characterController()
    weaponController = weaponController()
    buffController = buffController()
    damageCalculator = damageCalculator()
    buffController.loadBuffs()
    displayWeapons = []
    graphingCharacters = []
    loadedCharacterIndex = -1
    
    graph = scrollingGraph()
    

    # drawlimit for the graph in seconds
    drawLimit = 6

    startTime = 0
    timer = 0

    deltaTime = 0
    beforeTime = 0#time.time()
    screenDeltaTime = 0
    screenBeforeTime = 0#time.time()

    attacking = False
    graphType = "Standard"

    def initialise(self, root):
        self.icons["characterColourEntry"].bindFunctionToKeypress(self.setCharacterColour)
        self.icons["graphTypeOptionBox"].bindFunctionToKeypress(lambda *args : self.setGraphType())
        self.refreshList()
        self.graph.graphType = "Standard"
        self.initialiseGraph()
        self.graph.drawAxis()

    def refreshList(self):
        self.loadCharacters()
        self.displayCharacterChoices()

    def reload(self, root):
        self.refreshList()
        for i in range(len(self.graphingCharacters)):
            for x in self.characters:
                if self.graphingCharacters[i].characterId == x.characterId:
                    x.damageStats = self.graphingCharacters[i].damageStats
                    self.graphingCharacters[i] = x
                    self.characterController.generateStatPoints(x)
                    break
        self.displayLoadedCharacters()
        if self.loadedCharacterIndex != -1:
            self.loadedCharacter = self.graphingCharacters[self.loadedCharacterIndex]
            self.displayCharacterName()
            self.displayCharacterWeapon()
            self.displayCharacterClass()

    def setLoadedCharacterAndPopUpMenu(self, popUpFunction):
        if self.loadedCharacterIndex != -1:
            self.saveCharacter()
            popUpFunction()

    def displayCharacterChoices(self):
        self.icons["charactersListBox"].clear()
        for i in self.characters:
            self.icons["charactersListBox"].append(f"{i.name} - {i.characterClass} - lvl:{i.level}")

    def loadCharacterToBeGraphed(self):
        index = self.icons["charactersListBox"].getIndex()
        if len(index) == 0:
            return None
        index = index[0]
        self.graphingCharacters.append(self.characters[index])
        self.displayLoadedCharacters()
        pc = pointCollection(self.characters[index])
        self.graph.pointCollectionList.append(pc)
        self.characters[index].damageStats = damageStats(pc)

    def displayLoadedCharacters(self):
        self.icons["loadedCharactersListBox"].clear()
        for i in self.graphingCharacters:
            self.icons["loadedCharactersListBox"].append(f"{i.name} - {i.characterClass} - lvl:{i.level}")

    def loadCharacterForViewing(self):
        index = self.icons["loadedCharactersListBox"].getIndex()
        if len(index) == 0:
            return None
        self.loadedCharacterIndex = index[0]
        self.loadedCharacter = self.graphingCharacters[self.loadedCharacterIndex]
        self.displayCharacterName()
        self.displayCharacterWeapon()
        self.displayCharacterClass()
        self.displayCharacterColour()

    def displayCharacterName(self):
        self.icons["characterNameDisplayLabel"].set(self.loadedCharacter.name)

    def displayCharacterWeapon(self):
        self.icons["weaponLabel"].set(self.loadedCharacter.weapon.name)

    def displayCharacterClass(self):
        self.icons["classLabel"].set(self.loadedCharacter.characterClass)

    def displayCharacterColour(self):
        self.icons["characterColourEntry"].set(self.loadedCharacter.colour)

    def setCharacterColour(self):
        self.loadedCharacter.colour = self.icons["characterColourEntry"].get()
        self.graph.pointCollectionList[self.loadedCharacterIndex].updateColour(self.loadedCharacter.colour)
        self.saveCharacter()

    def removeCharacter(self):
        if self.loadedCharacterIndex == -1:
            return None
        for i in self.graph.pointCollectionList:
            if i.characterId == self.loadedCharacter.characterId:
                self.graph.pointCollectionList.remove(i)
                break
        self.graphingCharacters.pop(self.loadedCharacterIndex)
        self.displayLoadedCharacters()

    def initialiseGraph(self):
        self.graph.initialise(self.icons["displayCanvas"])
        self.graph.setOrigin(50, 370)
        self.graph.setDimensions(510, 350)
        self.graph.setXaxisLabel("Time")
        self.graph.setYaxisLabel("Damage")
        self.graph.setDrawLimit(self.drawLimit)

    def startGraphing(self):
        self.beforeTime = time.time()
        self.screenBeforeTime = self.beforeTime
        self.startTime = self.beforeTime
        self.timer = 0
        self.startAttacking()
        self.startRunning()
    
    def startAttacking(self):
        self.attacking = True
        for i in self.graph.pointCollectionList:
            i.pointXList = []
            i.pointYList = []
            i.lastPointTime = self.timer - self.drawLimit
    
    def stopGraphing(self):
        self.attacking = False
        self.stopRunning()

    def update(self):
        if self.attacking:
            self.deltaTime = time.time() - self.beforeTime
            self.beforeTime = time.time()

            self.timer += self.deltaTime

            self.graph.setTimer(self.timer)
            self.attack()
            #self.graph.garbageCollectPoints()

            self.screenDeltaTime = time.time() - self.screenBeforeTime
            if self.screenDeltaTime > 0.016:
                self.screenBeforeTime = time.time()
                self.icons["displayCanvas"].clear()
                if self.graphType == "Standard":
                    self.graph.setDrawLimit(self.drawLimit)
                    self.icons["displayCanvas"].write(570, 1, "Average", "n")
                    self.icons["displayCanvas"].write(570, 13, "dps", "n")
                    self.icons["displayCanvas"].write(535, 1, "Dps", "n")
                    self.icons["displayCanvas"].write(500, 1, "Total", "n")
                    self.icons["displayCanvas"].write(500, 13, "Average", "n")
                    self.icons["displayCanvas"].write(500, 25, "dmg", "n")
                    self.icons["displayCanvas"].write(455, 1, "Recent", "n")
                    self.icons["displayCanvas"].write(455, 13, "Average", "n")
                    self.icons["displayCanvas"].write(455, 25, "dmg", "n")
                    self.icons["displayCanvas"].write(420, 1, "Total", "n")
                    self.icons["displayCanvas"].write(420, 13, "dmg", "n")
                    for i in range(len(self.graphingCharacters)):
                        #dmg
                        self.icons["displayCanvas"].write(380, 38 + 12 * i, self.graphingCharacters[i].name, "n")
                        self.icons["displayCanvas"].write(570, 38 + 12 * i, self.graphingCharacters[i].damageStats.getTotalDps(self.timer), "n")
                        self.icons["displayCanvas"].write(535, 38 + 12 * i, self.graphingCharacters[i].damageStats.getDps(self.timer, self.drawLimit), "n")
                        self.icons["displayCanvas"].write(500, 38 + 12 * i, self.graphingCharacters[i].damageStats.getTotalAverageDamage(), "n")
                        self.icons["displayCanvas"].write(455, 38 + 12 * i, self.graphingCharacters[i].damageStats.getAverageDamage(self.timer, self.drawLimit), "n")
                        self.icons["displayCanvas"].write(420, 38 + 12 * i, self.graphingCharacters[i].damageStats.getTotalDmg(), "n")
                        #buffs
                        self.icons["displayCanvas"].write(100, 38 + 12 * i, self.graphingCharacters[i].name, "n")
                        for x in range(len(self.graphingCharacters[i].buffTimers)):
                            self.icons["displayCanvas"].write(140, 38 + 12 * i + 12 * x, self.graphingCharacters[i].buffTimers[x].name, "n")
                else:
                    self.graph.setDrawLimit(self.timer)
                self.graph.updateCanvas()


    def attack(self):
        if self.attacking:
            for x in range(len(self.graphingCharacters)):
                self.buffController.updateBuffs(self.graphingCharacters[x], self.deltaTime)
                if self.timer - self.graph.pointCollectionList[x].lastPointTime > self.graphingCharacters[x].weapon.hitInterval:
                    if self.buffController.checkToApplyBuffs(self.graphingCharacters[x]):
                        self.graph.pointCollectionList[x].lastPointTime = self.timer + 0.5 - self.graphingCharacters[x].weapon.hitInterval
                    else:
                        hitList = self.damageCalculator.getDamageFromHit(self.characterController, self.buffController, self.graphingCharacters[x])
                        dmg = 0
                        for i in hitList:
                            dmg += i.getDmg()
                        self.addPoint(x, dmg)
                        self.graph.pointCollectionList[x].lastPointTime = self.timer
            

    def displayGraphType(self):
        self.icons["graphTypeOptionBox"].set(self.graphType)

    def setGraphType(self):
        self.graphType = self.icons["graphTypeOptionBox"].get()
        if self.graphType == "Standard":
            self.graph.graphType = "Standard"
        else:
            self.graph.graphType = "Cumulative"

    def addPoint(self, index, damage):
        if self.graphType == "Standard":
            value = damage
        else:
            if len(self.graph.pointCollectionList[index].pointYList) == 0:
                value = damage
            else:
                value = self.graph.pointCollectionList[index].pointYList[-1] + damage
        self.graph.addPoint(index, self.timer, value)
        
