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
        "intelligence" : 0,
        "health" : 0,
        "melee damage" : 0,
        "move speed" : 0,
        "ranged damage" : 0,
        "mana" : 0,
        "magic damage" : 0
    }
    
    statPointDistribution = {
        "constitution" : 0,
        "strength" : 0,
        "agility" : 0,
        "dexterity" : 0,
        "wisdom" : 0,
        "intelligence" : 0
    }

        
class characterController:
    def new():
        c = character()
        c.level = 30
        characterController.generateStatPoints(c)
        return c

    def generateStatPoints(character):
        character.statPoint["strength"] = 10 + ((character.level-1) * 7)
