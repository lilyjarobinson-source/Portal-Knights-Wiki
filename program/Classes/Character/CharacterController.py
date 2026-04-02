class character:
    armour = {
        "head" : None,
        "torso" : None,
        "arms" : None,
        "legs" : None,
        "cape" : None,
        "ring" : None
    }
    weapon = None
    level = 1
    CharacterClass = None
    statPoint = {
        "constitution" : 0,
        "strength" : 0,
        "agility" : 0,
        "dexterity" : 0,
        "wisdom" : 0,
        "intelligence" : 0
    }
    
    statPointDistribution = {
        "constitution" : 0,
        "strength" : 0,
        "agility" : 0,
        "dexterity" : 0,
        "wisdom" : 0,
        "intelligence" : 0
    }

        
def characterController:
    def generateStatPoints(self, character):
        character.statPoint["strength"] = 10 + character.level * 7
