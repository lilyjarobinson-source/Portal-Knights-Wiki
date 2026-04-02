from Graph import graph
class scrollingGraph(graph):
    timer = 0
    drawLimit = 0

    def setDrawLimit(self, limit):
        self.drawLimit = limit

    def updateCanvas(self):
        self.canvas.clear()
        self.drawGraph()
        self.canvas.write(self.originX + self.width, self.originY + 10, f"{self.timer:.2f}", "n")
        self.canvas.write(self.originX, self.originY + 10, f"{self.timer-self.drawLimit:.2f}", "n")
        self.drawPoints()

    def drawXGrating(self):
        for i in range(int(self.timer-self.drawLimit+1), int(self.timer)+1):
            position = self.originX+self.width-((self.width/self.drawLimit) * (self.timer - i))
            self.canvas.line(position, self.originY, position, self.originY+10)
            self.canvas.write(position, self.originY+10, i, "n")

    def drawPoints(self):
        self.getPointsToDraw()
        self.generateYaxisScale()
        for i in range(len(self.drawList)):
            self.canvas.dot(
                self.originX+self.width-((self.width/self.drawLimit) * (self.timer - self.pointXList[self.drawList[i]])),
                self.originY-(self.height * self.pointYList[self.drawList[i]]/self.yAxisScale),
            )
            self.canvas.write(
                self.originX+self.width-((self.width/self.drawLimit) * (self.timer - self.pointXList[self.drawList[i]])),
                self.originY-(self.height * self.pointYList[self.drawList[i]]/self.yAxisScale),
                self.pointYList[self.drawList[i]],
                "sw"
            )

            
    
    def getPointsToDraw(self):
        self.drawList = []
        for i in range(len(self.pointXList)-1, 0, -1):
            if self.timer - self.pointXList[i] < self.drawLimit:
                self.drawList.append(i)
            else:
                break
        

    def setTimer(self, timer):
        self.timer = timer
    
    def addPoint(self, x, y):
        self.pointXList.append(x)
        self.pointYList.append(y)

    def generateYaxisScale(self):
        highestPoint = 0
        for i in self.drawList:
            if self.pointYList[i] > highestPoint:
                highestPoint = self.pointYList[i]
        print(highestPoint)
        self.yAxisScale = int(highestPoint * 1.2)
            

    def garbageCollectPoints(self):
        for i in range(len(self.pointXList)):
            if self.timer - self.pointXList[0] > self.drawLimit + 1.5:
                self.pointXList.pop(0)
                self.pointYList.pop(0)
            else:
                break
