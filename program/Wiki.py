import sys
classPath = __file__.split(__file__.split("\\")[-1])[0]
sys.path.append(classPath + "Menus\\")
sys.path.append(classPath + "Menus\\dmgCalculationMenus")
sys.path.append(classPath + "Menus\\characterMenus")
sys.path.append(classPath + "Menus\\framework")
sys.path.append(classPath + "Menus\\main-menus")
sys.path.append(classPath + "Classes\\Data-objects")
sys.path.append(classPath + "Classes\\Simulation")
sys.path.append(classPath + "Classes\\Graphing")
from Main import main

from Menu import menu, button, label, entry, optionBox, listBox, canvas, image

from MainMenu import mainMenu
from DmgCalcMenu import dmgCalcMenu
from CharacterOptionsMenu import characterOptionsMenu
from CharacterAttributeMenu import characterAttributeMenu
from CharacterNewMenu import characterNewMenu
from CharacterTalentMenu import characterTalentMenu
from CharacterArmourMenu import characterArmourMenu
from CharacterWeaponMenu import characterWeaponMenu
from CharacterOverviewMenu import characterOverviewMenu
from CharacterBuffMenu import characterBuffMenu
#'''
main = main("wiki", "800x500")

mainMenu = mainMenu()
dmgCalcMenu = dmgCalcMenu()
characterOptionsMenu = characterOptionsMenu()
characterAttributeMenu = characterAttributeMenu()
characterNewMenu = characterNewMenu()
characterTalentMenu = characterTalentMenu()
characterArmourMenu = characterArmourMenu()
characterWeaponMenu = characterWeaponMenu()
characterOverviewMenu = characterOverviewMenu()
characterBuffMenu = characterBuffMenu()

dmgCalcMenu.setRunable()

classes = ["warrior", "ranger", "mage", "rogue", "druid"]
graphTypes = ["Standard", "Cumulative"]

mainMenu.assignIcons({
    "dmgCalcMenuButton" : button([1, 60], [100, 19], "Damage simulator"),
    "characterEditingMenusButton" : button([1, 80], [100, 19], "Character editing"),
})

dmgCalcMenu.assignIcons({
    "backButton" : button([699, 1], [100, 19], "Back"),
    "displayCanvas" : canvas([201, 60], [598, 400]),

    "charcterMenuButton" : button([1, 60], [199, 19], "Characters menu"),
    
    "startGraphingButton" : button([1, 80], [99, 19], "Start graphing"),
    "stopGraphingButton" : button([101, 80], [99, 19], "Stop graphing"),
    
    "characterNameLabel" : label([1, 100], [40, 19], "Name"),
    "characterNameDisplayLabel" : label([42, 100], [158, 19], ""),
    "characterColourLabel" : label([1, 120], [50, 19], "Colour"),
    "characterColourEntry" : entry([52, 120], [48,  19]),
    "classLabel" : label([101, 120], [99, 19], ""),
    "weaponLabel" : label([1, 140], [199, 19], ""),
    "characterEditButton" : button([1, 160], [99, 19], "Edit"),
    "characterRemoveButton" : button([101, 160], [99, 19], "Remove"),
    
    "loadedCharactersListBoxLabel" : label([1, 180], [199, 19], "Loaded characters"),
    "loadedCharactersListBox" : listBox([1, 200], [199, 74]),
    
    "charactersListBoxLabel" : label([1, 280], [199, 19], "Select characters"),
    "charactersListBox" : listBox([1, 300], [199, 160]),

    "graphTypeLabel" : label([600, 40], [99, 19], "Graph type"),
    "graphTypeOptionBox" : optionBox([700, 40], [99, 19], graphTypes[0], graphTypes),
})
charMenuNavigationButtons = {
    "OverviewButton" : button([1, 1], [65, 30], "Overview"),
    "levelButton" : button([67, 1], [66, 30], "Level"),
    "weaponButton" : button([134, 1], [66, 30], "Weapon"),
    "armourButton" : button([201, 1], [66, 30], "Armour"),
    "buffButton" : button([268, 1], [66, 30], "Buffs"),
    "optionsButton" : button([335, 1], [65, 30], "Options"),
}
charMenuNavigationButtons["OverviewButton"].bindFunction(lambda : main.changeMenu("characterOverviewMenu"))
charMenuNavigationButtons["levelButton"].bindFunction(lambda : main.changeMenu("characterAttributeMenu"))
charMenuNavigationButtons["weaponButton"].bindFunction(lambda : main.changeMenu("characterWeaponMenu"))
charMenuNavigationButtons["armourButton"].bindFunction(lambda : main.changeMenu("characterArmourMenu"))
charMenuNavigationButtons["buffButton"].bindFunction(lambda : main.changeMenu("characterBuffMenu"))
charMenuNavigationButtons["optionsButton"].bindFunction(lambda : main.changeMenu("characterOptionsMenu"))

characterOptionsMenu.assignIcons({
    "selectCharButton" : button([1, 60], [100, 19], "Select character"),
    "saveCharButton" : button([1, 80], [100, 19], "Save character"),
    "loadCharsButton" : button([1, 100], [100, 19], "Refresh List"),
    "newCharButton" : button([1, 120], [100, 19], "New character"),
    "deleteCharButton" : button([1, 140], [100, 19], "Delete character"),

    "charactersListBox" : listBox([199, 60], [201, 189]),
})

characterAttributeMenu.assignIcons({
    "frameLabel" : label([1, 55], [399, 194], ""),
    
    "attributeLabel" : label([3, 100], [89, 19], "Attribute"),
    "attributeBaseLabel" : label([93, 100], [40, 19], "Base"),
    "attributeExtraLabel" : label([134, 100], [40, 19], "Extra"),
    "attributeTotalLabel" : label([175, 100], [40, 19], "Total"),
    "statLabel" : label([216, 100], [100, 19], "Stat"),
    "statBaseLabel" : label([317, 100], [40, 19], "Base"),
    "statTotalLabel" : label([358, 100], [40, 19], "Total"),

    "classLabel" : label([50, 60], [40, 19], "Class"),
    "classOptionBox" : optionBox([30, 80], [80, 19], "", classes),

    "remainingAttributePointsLabel" : label([300, 60], [92, 19], "Attribute points"),
    "remainingAttributePointsDisplayLabel" : label([325, 80], [40, 19], ""),
})

characterTalentMenu.assignIcons({
    "frameLabel" : label([1, 55], [399, 194], ""),
    
    "talentLabel" : label([3, 60], [50, 19], "Talents"),
    
    "classLabel" : label([338, 60], [40, 19], "Class"),
    "classOptionBox" : optionBox([318, 80], [80, 19], "", classes),
})

characterArmourMenu.assignIcons({
    "armourLabel" : label([1, 40], [99, 19], "Armour"),
    "defenceLabel" : label([101, 40], [60, 19], "Defence"),
    "defenceDisplayLabel" : label([162, 40], [38, 19], ""),
    
    "armourListBox" : listBox([201, 60], [199, 189]),
    
    "nameLabel" : label([1, 180], [199, 19], ""),
    "buffLabel" : label([1, 200], [199, 19], ""),
    "multiplierListBox" : listBox([1, 220], [199, 29]),
})

armourSlots = ["Head", "Torso", "Arms", "Legs", "Cape", "Ring"]
for i in range(6):
    characterArmourMenu.addIcons({
        f"{armourSlots[i].lower()}Label" : label([1, 60 + i * 20], [40, 19], armourSlots[i]),
        f"{armourSlots[i].lower()}Entry" : entry([42, 60 + i * 20], [158, 19]),
    })
unlockLevels = [2, 5, 10, 15, 20, 25, 30]
for i in range(7):
    characterTalentMenu.addIcons({
        f"level{i}Label" : label([3, 80 + i * 20], [30, 19], unlockLevels[i]),
        f"talent{i}OptionBox" : optionBox([34, 80 + i * 20], [150, 19], "", [""])
    })

for i in [characterAttributeMenu, characterTalentMenu]:
    i.addIcons({
        "attributesButton" : button([1, 35], [80, 19], "Attributes"),
        "talentButton" : button([82, 35], [80, 19], "Talents"),

        "levelLabel" : label([317, 35], [42, 19], "Level"),
        "levelEntry" : entry([360, 35], [40, 19]),
    })
    i.icons["attributesButton"].bindFunction(lambda : main.changeMenu("characterAttributeMenu"))
    i.icons["talentButton"].bindFunction(lambda : main.changeMenu("characterTalentMenu"))


attributes = ["Constitution", "Strength", "Agility", "Dexterity", "Wisdom", "Intelligence"]
for i in range(6):
    characterAttributeMenu.addIcons({
        f"{attributes[i].lower()}Button" : button([3, 128 + i * 20], [89, 19], attributes[i]),
        f"{attributes[i].lower()}BaseLabel" : label([93, 128 + i * 20], [40, 19], ""),
        f"{attributes[i].lower()}AssignedPointsEntry" : entry([134, 128 + i * 20], [40, 19]),
        f"{attributes[i].lower()}TotalLabel" : label([175, 128 + i * 20], [40, 19], ""),
    })
    
stats = ["Health", "Melee damage", "Movement speed", "Ranged damage", "Mana", "Magic damage"]
for i in range(6):
    characterAttributeMenu.addIcons({
        f"{stats[i].lower()}Label" : label([216, 128 + i * 20], [100, 19], stats[i]),
        f"{stats[i].lower()}BaseLabel" : label([317, 128 + i * 20], [40, 19], ""),
        f"{stats[i].lower()}TotalLabel" : label([358, 128 + i * 20], [40, 19], ""),
    })
 
characterNewMenu.assignIcons({
    "nameLabel" : label([1, 60], [60, 19], "Name:"),
    "classLabel" : label([1, 80], [60, 19], "Class:"),
    
    "nameEntry" : entry([62, 60], [200, 19]),
    "classOptionBox" : optionBox([62, 80], [200, 19], "warrior", classes),

    "createCharacterButton" : button([1, 120], [124, 39], "Create"),

    "backButton" : button([300, 1], [100, 19], "Back")
})

filters = ["Name", "Damage", "Stat", "Buff"]
characterWeaponMenu.assignIcons({
    "weaponListBox" : listBox([201, 60], [199, 189]),

    "nameLabel" : label([1, 40], [199, 19], ""),
    "weaponTypeLabel" : label([1, 60], [99, 19], ""),
    "dmgTypeLabel" : label([101, 60], [99, 19], ""),
    "damageLabel" : label([1, 80], [60, 19], "Damage"),
    "damageDisplayLabel" : label([62, 80], [38, 19], ""),
    "defenceLabel" : label([101, 80], [60, 19], "Defence"),
    "defenceDisplayLabel" : label([162, 80], [38, 19], ""),
    "buffLabel" : label([1, 100],  [199, 19], ""),
    "statListBox" : listBox([1, 120], [199, 39]),

    "filterResetButton" : button([1, 200], [99, 19], "Reset filters"),
    "filterApplyButton" : button([101, 200], [99, 19], "Apply filter"),
    "filterOptionMenu" : optionBox([1, 160], [99, 19], filters, "Name"),
    "filterEntryBox" : entry([1, 180], [199, 19]),
    "filterTypeOptionMenu" : optionBox([101, 160], [99, 19], ["itemAssetName"], "Includes"),
    "filtersDisplayListbox" : listBox([1, 220], [199, 29]),

    #"filterDamageFromEntry" : entry([1, 180], [81, 19]),
    #"filterDamageToEntry" : entry([119, 180], [81, 19]),
    #"filterDamageLabel" : label([83, 180], [35, 19], "->"),
})

characterOverviewMenu.assignIcons({
    "backButton" : button([699, 1], [100, 19], "Back"),
    "canvas" : canvas([1, 21], [798, 478]),
})

characterBuffMenu.assignIcons({
    "buffListBox" : listBox([1, 60], [199, 189]),
    "selectedBuffListBox" : listBox([201, 60], [199, 189]),
})

for i in [characterArmourMenu, characterWeaponMenu]:
    i.addIcons({
        "classLabel" : label([201, 40], [99, 19], "Class"),
        "classOptionBox" : optionBox([301, 40], [99, 19], "", classes),
    })


for i in [characterAttributeMenu, characterTalentMenu, characterArmourMenu, characterWeaponMenu, characterOverviewMenu, characterBuffMenu]:
    i.addIcons(charMenuNavigationButtons)

main.addMenus([mainMenu, dmgCalcMenu, characterOptionsMenu, characterOverviewMenu, characterNewMenu, characterAttributeMenu, characterTalentMenu, characterWeaponMenu, characterArmourMenu, characterBuffMenu])
main.ignoreIconFile()
main.activate("characterOverviewMenu")
main.root.mainloop()
#'''
