class pointCollection:
    hexDigits = "0123456789abcdef"
    def __init__(self, c):
        self.characterId = c.characterId
        self.pointXList = []
        self.pointYList = []
        self.drawList = []
        self.colour = self.setColour(c.colour)
        self.lastPointTime = 0
        
    def setColour(self, colour):
        if len(colour) == 0:
            return "#000000"
        if colour[0] == "#":
            colour = colour[1:]
        if len(colour) < 6:
            return "#000000"
        result = "#"
        for i in colour:
            if i not in pointCollection.hexDigits:
                return "#000000"
            result += i
        return result

    def updateColour(self, colour):
        self.colour = self.setColour(colour)
        
        
