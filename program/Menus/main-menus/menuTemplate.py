import sys, time
classPath = __file__.split("Menus")[0]
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Classes\\DmgCalculation")
sys.path.append(classPath + "Classes\\Graphing")
sys.path.append(classPath + "Menus\\framework")
from DamageCalculator import damageCalculator
from WeaponController import weaponController
from CharacterController import characterController
from Graph import graph
from ScrollingGraph import scrollingGraph
from Menu import menu
from CharacterMenuTemplate import characterMenuTemplate

class dmgCalcMenu(menu):
    characterController = characterController()
    weaponController = weaponController()
    damageCalculator = damageCalculator()
    weapons = []
    loadedWeaponIndex = -1
    loadedCharacter = characterController.new()
    
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

    lastAttackTime = 0

    def initialise(self, root):
        self.graph.initialise(self.icons["displayCanvas"])
        self.graph.setOrigin(50, 370)
        self.graph.setDimensions(510, 350)
        self.graph.setXaxisLabel("Time")
        self.graph.setYaxisLabel("Damage")
        self.graph.setDrawLimit(self.drawLimit)
        #self.startGraphing()
        self.weaponController.loadWeapons()
        self.displayWeapons()

    def startGraphing(self):
        self.beforeTime = time.time()
        self.screenBeforeTime = self.beforeTime
        self.startTime = self.beforeTime
        self.timer = 0
        self.startAttacking()

    def stopAttacking(self):
        self.attacking = False

    def update(self):
        if self.attacking:
            self.deltaTime = time.time() - self.beforeTime
            self.beforeTime = time.time()

            self.timer += self.deltaTime

            self.graph.setTimer(self.timer)
            self.attack()
            self.graph.garbageCollectPoints()

            self.screenDeltaTime = time.time() - self.screenBeforeTime
            if self.screenDeltaTime > 0.016:
                self.screenBeforeTime = time.time()
                self.graph.updateCanvas()

    def startAttacking(self):
        self.attacking = True
        self.lastAttackTime = self.timer - self.drawLimit

        if self.loadedWeaponIndex == -1:
            self.loadedWeaponIndex = self.icons["weaponListBox"].getItems().index("Fist")
            self.loadedCharacter.weapon = self.weapons[self.loadedWeaponIndex]

    def attack(self):
        if self.attacking:
            if self.timer - self.lastAttackTime > self.loadedCharacter.weapon.wpnType.attackInterval:
                hitList = self.damageCalculator.getDamageFromHit(self.loadedCharacter)
                dmg = 0
                for i in hitList:
                    dmg += i.getDmg()
                
                self.graph.addPoint(self.timer, dmg)
                self.lastAttackTime = self.timer

    def displayWeapons(self):
        self.weapons = self.weaponController.getWeapons()
        for i in self.weapons:
            self.icons["weaponListBox"].append(i.name)

    def loadWeapon(self):
        index = self.icons["weaponListBox"].getIndex()
        if len(index) == 0:
            return
        self.loadedWeaponIndex = index[0]
        self.loadedCharacter.weapon = self.weapons[index[0]]
















