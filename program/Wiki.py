import sys
classPath = __file__.split(__file__.split("\\")[-1])[0]
sys.path.append(classPath + "Menus\\main-menus")
sys.path.append(classPath + "Menus\\popup-menus")
sys.path.append(classPath + "Menus\\framework")
sys.path.append(classPath + "Menus\\main-menus")
sys.path.append(classPath + "Classes\\Data-objects")
from Main import main
from PopupMenu import popupMenu

from Menu import menu, obj, button, label, entry, optionBox, listBox, canvas, image

from DmgCalcMenu import dmgCalcMenu
from CharacterOptionsMenu import characterOptionsMenu
from CharacterAttributeMenu import characterAttributeMenu
from CharacterNewMenu import characterNewMenu
from CharacterTalentMenu import characterTalentMenu
#'''
main = main("wiki", "800x500")
characterEditorPopup = popupMenu("Character editor", "401x250")

dmgCalcMenu = dmgCalcMenu(True)
characterOptionsMenu = characterOptionsMenu()
characterAttributeMenu = characterAttributeMenu()
characterNewMenu = characterNewMenu()
characterTalentMenu = characterTalentMenu()

classes = ["Warrior", "Ranger", "Mage", "Rogue", "Druid"]

dmgCalcMenu.assignIcons({
    "displayCanvas" : canvas([200, 60], [599, 400]),
    "weaponListBox" : listBox([1, 100], [201, 160], lambda *args : dmgCalcMenu.loadWeapon()),
    "attackButton" : button([100, 80], [100, 19], "Start attacking", dmgCalcMenu.startGraphing),
    "menuButton" : button([100, 100], [100, 19], "menu", lambda : main.popUpMenu(0)),
})
charMenuNavigationButtons = {
    "levelButton" : button([1, 1], [99, 30], "level", lambda : characterEditorPopup.changeMenu(1)),
    "optionsButton" : button([301, 1], [99, 30], "options", lambda : characterEditorPopup.changeMenu(0)),
    "armourButton" : button([101, 1], [99, 30], "armour", lambda : characterEditorPopup.changeMenu(0)),
    "weaponButton" : button([201, 1], [99, 30], "weapon", lambda : characterEditorPopup.changeMenu(0)),
}

characterOptionsMenu.assignIcons({
    "selectCharButton" : button([1, 60], [100, 19], "Select character", lambda : characterOptionsMenu.selectCharacter(characterEditorPopup)),
    "saveCharButton" : button([1, 80], [100, 19], "Save character", characterOptionsMenu.saveCharacter),
    "loadCharsButton" : button([1, 100], [100, 19], "Refresh List", characterOptionsMenu.refreshList),
    "newCharButton" : button([1, 120], [100, 19], "New character", lambda : characterEditorPopup.changeMenu(2)),
    "deleteCharButton" : button([1, 140], [100, 19], "Delete character", characterOptionsMenu.deleteCharacter),

    "charactersListbox" : listBox([199, 60], [201, 189], None),
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
    "classOptionBox" : optionBox([30, 80], [80, 19], classes, ""),
})

characterTalentMenu.assignIcons({
    "canvas" : canvas([1, 55], [399, 194]),
})

for i in [characterAttributeMenu, characterTalentMenu]:
    i.addIcons({
        "attributesButton" : button([1, 35], [80, 19], "Attributes", lambda : characterEditorPopup.changeMenu(1)),
        "talentButton" : button([82, 35], [80, 19], "Talents", lambda : characterEditorPopup.changeMenu(3)),

        "levelLabel" : label([317, 35], [42, 19], "Level"),
        "levelEntry" : entry([360, 35], [40, 19]),
    })

attributes = ["Constitution", "Strength", "Agility", "Dexterity", "Intelligence", "Wisdom"]
for i in range(6):
    characterAttributeMenu.addIcons({
        f"{attributes[i].lower()}Button" : button([3, 128 + i * 20], [89, 19], attributes[i], None),
        f"{attributes[i].lower()}BaseLabel" : label([93, 128 + i * 20], [40, 19], "", None),
        f"{attributes[i].lower()}AssignedPointsEntry" : entry([134, 128 + i * 20], [40, 19]),
        f"{attributes[i].lower()}TotalLabel" : label([175, 128 + i * 20], [40, 19], "", None),
    })
    
stats = ["Health", "Melee damage", "Movement speed", "Ranged damage", "Magic damage", "Mana"]
for i in range(6):
    characterAttributeMenu.addIcons({
        f"{stats[i].lower()}Label" : label([216, 128 + i * 20], [100, 19], stats[i], None),
        f"{stats[i].lower()}BaseLabel" : label([317, 128 + i * 20], [40, 19], "", None),
        f"{stats[i].lower()}TotalLabel" : label([358, 128 + i * 20], [40, 19], "", None),
    })
 
characterNewMenu.assignIcons({
    "nameLabel" : label([1, 60], [60, 19], "Name:"),
    "classLabel" : label([1, 80], [60, 19], "Class:"),
    
    "nameEntry" : entry([62, 60], [200, 19]),
    "classOptionBox" : optionBox([62, 80], [200, 19], classes, "warrior"),

    "createCharacterButton" : button([1, 120], [124, 39], "Create", lambda : characterNewMenu.createCharacter(characterEditorPopup))
})



characterEditorPopup.assignMenus([characterOptionsMenu, characterAttributeMenu, characterNewMenu, characterTalentMenu])

for i in [characterAttributeMenu, characterNewMenu, characterTalentMenu]:
    i.addIcons(charMenuNavigationButtons)

main.assignMenus([dmgCalcMenu])
main.assignPopupMenus([characterEditorPopup])
#main.popUpMenu(0)
#characterEditorPopup.changeMenu(3)
main.activate()
#main.root.mainloop()
#'''
