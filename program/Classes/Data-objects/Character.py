class character:
    characterId = ""
    name = ""
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
    characterClass = ""
    unspentAttributePoints = 0
    attributePoint = {
        "constitution" : 0,
        "strength" : 0,
        "agility" : 0,
        "dexterity" : 0,
        "wisdom" : 0,
        "intelligence" : 0,
    }
    statPoint = {
        "health" : 0,
        "melee damage" : 0,
        "move speed" : 0,
        "ranged damage" : 0,
        "mana" : 0,
        "magic damage" : 0
    }
    
    attributePointDistribution = {
        "constitution" : 0,
        "strength" : 0,
        "agility" : 0,
        "dexterity" : 0,
        "wisdom" : 0,
        "intelligence" : 0
    }

