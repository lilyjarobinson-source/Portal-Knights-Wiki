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
from CharacterLevelMenu import characterLevelMenu
from CharacterNewMenu import characterNewMenu
#'''
main = main("wiki", "800x500")
characterEditorPopup = popupMenu("Character editor", "401x250")

dmgCalcMenu = dmgCalcMenu(True)
characterOptionsMenu = characterOptionsMenu()
characterLevelMenu = characterLevelMenu()
characterNewMenu = characterNewMenu()

classes = ["warrior", "ranger", "mage", "rogue", "druid"]

dmgCalcMenu.assignIcons({
    "displayCanvas" : canvas([200, 60], [599, 400]),
    "weaponListBox" : listBox([1, 100], [201, 160], lambda *args : dmgCalcMenu.loadWeapon()),
    "attackButton" : button([100, 80], [100, 19], "Start attacking", dmgCalcMenu.startAttacking),
    "menuButton" : button([100, 100], [100, 19], "menu", lambda : main.popUpMenu(0)),
})
charMenuNavigationButtons = {
    "levelButton" : button([1, 1], [99, 30], "level", lambda : characterEditorPopup.changeMenu(1)),
    "optionsButton" : button([301, 1], [99, 30], "options", lambda : characterEditorPopup.changeMenu(0)),
    "armourButton" : button([101, 1], [99, 30], "armour", lambda : characterEditorPopup.changeMenu(0)),
    "weaponButton" : button([201, 1], [99, 30], "weapon", lambda : characterEditorPopup.changeMenu(0)),
}

characterOptionsMenu.assignIcons({
    "selectCharButton" : button([1, 60], [100, 19], "Select character", characterOptionsMenu.selectCharacter),
    "saveCharButton" : button([1, 80], [100, 19], "Save character", characterOptionsMenu.saveCharacter),
    "loadCharsButton" : button([1, 100], [100, 19], "Refresh List", characterOptionsMenu.refreshList),
    "newCharButton" : button([1, 120], [100, 19], "New character", lambda : characterEditorPopup.changeMenu(2)),
    "deleteCharButton" : button([1, 140], [100, 19], "Delete character", characterOptionsMenu.deleteCharacter),

    "charactersListbox" : listBox([199, 60], [201, 189], None),
})

characterLevelMenu.assignIcons({
    "frameLabel" : label([1, 98], [399, 151], ""),


    
    "statsLabel" : label([3, 100], [29, 100], "Stats"),
    "constitutionButton" : button([33, 100], [60, 100], "Con", None),
    "strengthButton" : button([94, 100], [60, 100], "Str", None),
    "agilityButton" : button([155, 100], [60, 100], "Agi", None),
    "dexterityButton" : button([216, 100], [60, 100], "Dex", None),
    "inteligenceButton" : button([277, 100], [60, 100], "Int", None),
    "wisdomButton" : button([338, 100], [60, 100], "Wis", None),
})

characterNewMenu.assignIcons({
    "nameLabel" : label([1, 60], [60, 19], "Name:"),
    "classLabel" : label([1, 80], [60, 19], "Class:"),
    
    "nameEntry" : entry([62, 60], [200, 19]),
    "classOptionBox" : optionBox([62, 80], [200, 19], classes, "warrior"),

    "createCharacterButton" : button([1, 120], [124, 39], "Create", lambda : characterNewMenu.createCharacter(characterEditorPopup))
})



characterEditorPopup.assignMenus([characterOptionsMenu, characterLevelMenu, characterNewMenu])

for i in characterEditorPopup.menus:
    i.addIcons(charMenuNavigationButtons)

main.assignMenus([dmgCalcMenu])
main.assignPopupMenus([characterEditorPopup])
main.popUpMenu(0)
characterEditorPopup.changeMenu(1)
main.activate()
main.root.mainloop()
#'''
