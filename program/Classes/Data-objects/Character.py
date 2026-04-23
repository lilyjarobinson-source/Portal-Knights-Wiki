class character:
    def __init__(self):
        self.characterId = ""
        self.name = ""
        self.armour = {
            "head" : None,
            "torso" : None,
            "arms" : None,
            "legs" : None,
            "cape" : None,
            "ring" : None
        }
        self.weapon = None
        self.level = 1
        self.characterClass = ""
        self.attributePoints = {
            "constitution" : 0,
            "strength" : 0,
            "agility" : 0,
            "dexterity" : 0,
            "wisdom" : 0,
            "intelligence" : 0,
        }
        self.statPoints = {
            "health" : 0,
            "melee damage" : 0,
            "movement speed" : 0,
            "ranged damage" : 0,
            "mana" : 0,
            "magic damage" : 0
        }
        
        self.attributePointDistribution = {
            "constitution" : 0,
            "strength" : 0,
            "agility" : 0,
            "dexterity" : 0,
            "wisdom" : 0,
            "intelligence" : 0
        }

    def setAttributePointAt(self, key, value):
        self.attributePoints[key] = value

    def setStatPointAt(self, key, value):
        self.statPoints[key] = value

    def setAttributePointDistributionAt(self, key, value):
        self.attributePointDistribution[key] = value

    def toString(self):
        return f"""character:
    id : {self.characterId}
    name : {self.name}
    armour : {self.armour}
    weapon : {self.weapon.toString()}
    level : {self.level}
    class : {self.characterClass}
    attributePoints : {self.attributePoints}
    statPoints : {self.statPoints}
    attributePointDistribution : {self.attributePointDistribution}"""

