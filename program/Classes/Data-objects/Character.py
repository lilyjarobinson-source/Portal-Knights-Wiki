class character:
    def __init__(self):
        self.characterId = ""
        self.name = ""
        self.armour = {
            "Head" : None,
            "Torso" : None,
            "Arms" : None,
            "Legs" : None,
            "Cape" : None,
            "Ring" : None
        }
        self.weapon = None
        self.level = 1
        self.characterClass = ""
        self.colour = ""
        self.attributePoints = {
            "constitution" : 0,
            "strength" : 0,
            "agility" : 0,
            "dexterity" : 0,
            "wisdom" : 0,
            "intelligence" : 0,
        }
        self.bonusAttributePoints = {
            "constitution" : 0,
            "strength" : 0,
            "agility" : 0,
            "dexterity" : 0,
            "wisdom" : 0,
            "intelligence" : 0,
        }
        self.baseStatPoints = {
            "health" : 0,
            "melee damage" : 0,
            "movement speed" : 0,
            "ranged damage" : 0,
            "mana" : 0,
            "magic damage" : 0
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
        self.talents = [0,0,0,0,0,0,0]
        self.armourMultipliers = {}
        self.damageStats = None
        self.buffTimers = {}
        self.hitCounter = 0

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

