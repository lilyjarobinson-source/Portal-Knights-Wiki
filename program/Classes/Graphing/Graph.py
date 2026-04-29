class graph:
    canvas = None
    
    originX = 0
    originY = 0
    width = 0
    height = 0

    pointCollectionList = []

    xAxisScale = 1
    yAxisScale = 1
    
    xGratingAmount = 4
    yGratingAmount = 4

    xAxisLabel = ""
    yAxisLabel = ""

    def initialise(self, canvas):
        self.canvas = canvas

    def setOrigin(self, originX, originY):
        self.originX = originX
        self.originY = originY

    def setDimensions(self, width, height):
        self.width = width
        self.height = height

    def setXaxisLabel(self, label):
        self.xAxisLabel = label

    def setYaxisLabel(self, label):
        self.yAxisLabel = label

    def drawGraph(self):
        self.drawAxis()
        self.drawXGrating()
        self.drawYGrating()

    def drawAxis(self):
        self.canvas.line(self.originX-10, self.originY, self.originX+self.width, self.originY)
        self.canvas.write(self.originX+self.width+20, self.originY, self.xAxisLabel)
        self.canvas.line(self.originX, self.originY-self.height, self.originX, self.originY+10)
        self.canvas.write(self.originX-5, self.originY-self.height-12, self.yAxisLabel)
        
        self.canvas.write(self.originX-13, self.originY, "0", "e")       
        self.canvas.line(self.originX+self.width, self.originY, self.originX+self.width, self.originY+10)

    def drawXGrating(self):
        for i in range(1, self.xGratingAmount+1):
            position = self.originX+self.width-(self.width * i/self.xGratingAmount)
            self.canvas.write(position, self.originY-10, f"{self.xAxisScale*i/self.xGratingAmount}", "n")
            self.canvas.line(position, self.originY, position, self.originY-10)

    def drawYGrating(self):
        for i in range(1, self.yGratingAmount+1):
            position = self.originY-(self.height * i/self.yGratingAmount)
            self.canvas.write(self.originX-13, position, f"{self.yAxisScale*i/self.yGratingAmount}", "e")
            self.canvas.line(self.originX-10, position, self.originX, position)

    def drawPoints(self):
        self.getPointsToDraw()
        for x in self.pointCollectionList:
            for i in range(len(x.drawList)-1):
                self.canvas.dot(
                    self.originX+self.width-(self.width * self.pointXList[x.drawList[i]]/self.xAxisScale),
                    self.originY-(self.height * self.pointYList[x.drawList[i]]/self.yAxisScale),
                    x.colour
                )

    def getPointsToDraw(self):
        for i in self.pointCollectionList:
            i.drawList = range(len(i.pointXList))

    def addPoint(self, pointCollectionIndex, x, y):
        self.pointCollectionList[pointCollectionIndex].pointXList.append(x)
        self.pointCollectionList[pointCollectionIndex].pointYList.append(y)
        
    
