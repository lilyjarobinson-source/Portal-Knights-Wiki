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
        for x in self.pointCollectionList:
            for i in range(len(x.drawList)):
                self.canvas.dot(
                    self.originX+self.width-((self.width/self.drawLimit) * (self.timer - x.pointXList[x.drawList[i]])),
                    self.originY-(self.height * x.pointYList[x.drawList[i]]/self.yAxisScale),
                    x.colour
                )
                self.canvas.write(
                    self.originX+self.width-((self.width/self.drawLimit) * (self.timer - x.pointXList[x.drawList[i]])),
                    self.originY-(self.height * x.pointYList[x.drawList[i]]/self.yAxisScale),
                    x.pointYList[x.drawList[i]],
                    "sw",
                )

            
    
    def getPointsToDraw(self):
        for x in self.pointCollectionList:
            x.drawList = []
            for i in range(len(x.pointXList)-1, 0, -1):
                if self.timer - x.pointXList[i] < self.drawLimit:
                    x.drawList.append(i)
                else:
                    break
        

    def setTimer(self, timer):
        self.timer = timer

    def generateYaxisScale(self):
        highestPoint = 0
        for x in self.pointCollectionList:
            for i in x.drawList:
                if x.pointYList[i] > highestPoint:
                    highestPoint = x.pointYList[i]
        self.yAxisScale = int(highestPoint * 1.2)
            

    def garbageCollectPoints(self):
        for x in self.pointCollectionList:
            for i in range(len(x.pointXList)):
                if self.timer - x.pointXList[0] > self.drawLimit + 1.5:
                    x.pointXList.pop(0)
                    x.pointYList.pop(0)
                else:
                    break
