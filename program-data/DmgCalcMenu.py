import time, random
from Menu import menu
from RunableMenu import runableMenu

class dmgCalcMenu(runableMenu):
    listOfHits = []
    listOfHitTimestamps = []
    drawList = []
    canvas = None

    # drawlimit for the graph in seconds
    drawLimit = 5
    # highest damage * 1.1
    yAxisScale = 1
    yAxisScaleAmount = 5

    hardestHit = 0

    startTime = 0
    timer = 0

    deltaTime = 0
    beforeTime = 0#time.time()
    screenDeltaTime = 0
    screenBeforeTime = 0#time.time()

    attacking = False

    lastAttackTime = 0
    # remove replace with a class
    attackInterval = 0.6

    def initialise(self, root):
        self.canvas = self.icons["displayCanvas"]
        self.startGraphing()

    def updateCanvas(self):
        self.canvas.clear()
        self.drawGraph()
        self.canvas.write(560, 380, f"{self.timer:.2f}", "n")
        self.canvas.write(50, 380, f"{self.timer-self.drawLimit:.2f}", "n")
        self.drawMovingTimes()
        self.drawDamageScale()
        self.drawHits()

    def drawGraph(self):
        self.canvas.line(50, 20, 50, 380)
        self.canvas.write(45, 10, "Damage")
        self.canvas.line(40, 370, 560, 370)
        self.canvas.write(580, 370, "Time")
        
        self.canvas.write(37, 370, "0", "e")       
        self.canvas.line(560, 370, 560, 380)

    def drawMovingTimes(self):
        for i in range(int(self.timer)-self.drawLimit+1, int(self.timer)+1):
            position = 560-((510/self.drawLimit) * (self.timer - i))
            self.canvas.line(position, 370, position, 380)
            self.canvas.write(position, 380, i, "n")

    def drawDamageScale(self):
        for i in range(1, self.yAxisScaleAmount+1):
            position = 370-(350 * i/self.yAxisScaleAmount)
            self.canvas.write(37, position, f"{self.yAxisScale*i/self.yAxisScaleAmount}", "e")
            self.canvas.line(40, position, 50, position)

    def drawHits(self):
        self.getHitsToDraw()
        for i in range(len(self.drawList)-1):
            self.canvas.line(
                560-((510/self.drawLimit) * (self.timer - self.listOfHitTimestamps[i])),
                370-(350 * self.listOfHits[i]/self.yAxisScale),
                560-((510/self.drawLimit) * (self.timer - self.listOfHitTimestamps[i+1])),
                370-(350 * self.listOfHits[i+1]/self.yAxisScale)
            )
        
    def getHitsToDraw(self):
        self.drawList = []
        for i in range(len(self.listOfHitTimestamps)-1, 0, -1):
            if self.timer - self.listOfHitTimestamps[i] < self.drawLimit:
                self.drawList.append(i)
            else:
                break
    
    def addHit(self, dmg):
        self.listOfHits.append(dmg)
        self.listOfHitTimestamps.append(self.timer)
        self.lastAttackTime = self.timer
        if dmg > self.hardestHit:
            self.hardestHit = dmg
            self.yAxisScale = int(self.hardestHit * 1.1)

    def garbageCollectHits(self):
        i = 0
        while i < len(self.listOfHitTimestamps) and self.timer - self.listOfHitTimestamps[i] > self.drawLimit:
            i += 1
        for x in range(i):
            self.listOfHits.pop(0)
            self.listOfHitTimestamps.pop(0)

    def startGraphing(self):
        self.beforeTime = time.time()
        self.screenBeforeTime = self.beforeTime
        self.startTime = self.beforeTime
        self.timer = 0

    def update(self):
        self.deltaTime = time.time() - self.beforeTime
        self.beforeTime = time.time()

        self.timer += self.deltaTime

        self.attack()
        self.garbageCollectHits()

        self.screenDeltaTime = time.time() - self.screenBeforeTime
        if (self.screenDeltaTime > 0.016):
            self.screenBeforeTime = time.time()
            self.updateCanvas()

    def startAttacking(self):
        self.attacking = True

    def attack(self):
        if self.attacking:
            if self.timer - self.lastAttackTime > self.attackInterval:
                self.addHit(random.randint(100, 200))
        
















