class damageStats:
    def __init__(self, pointCollection):
        self.pointCollection = pointCollection

    def setPointCollection(self, pointCollection):
        self.pointCollection = pointCollection

    def getTotalDps(self, timeElapsed):
        totalDmg = 0
        for i in self.pointCollection.pointYList:
            totalDmg += i
        return int(totalDmg / timeElapsed)

    def getDps(self, time, period):
        totalDmg = 0
        for i in range(len(self.pointCollection.pointXList)-1, 0, -1):
            if time - self.pointCollection.pointXList[i] < period:
                totalDmg += self.pointCollection.pointYList[i]
            else:
                break
        return int(totalDmg / period)

    def getAverageDamage(self, time, period):
        totalDmg = 0
        count = 0
        for i in range(len(self.pointCollection.pointXList)-1, 0, -1):
            if time - self.pointCollection.pointXList[i] < period:
                totalDmg += self.pointCollection.pointYList[i]
                count += 1
            else:
                break
        if count == 0:
            return 0
        return int(totalDmg / count)

    def getTotalAverageDamage(self):
        totalDmg = 0
        for i in self.pointCollection.pointYList:
            totalDmg += i
        if len(self.pointCollection.pointYList) == 0:
            return 0
        return int(totalDmg / len(self.pointCollection.pointYList))

    def getTotalDmg(self):
        totalDmg = 0
        for i in self.pointCollection.pointYList:
            totalDmg += i
        return totalDmg
        
