import sys
sys.path.append(__file__.split(__file__.split("\\")[-1])[0] + "Menus")
from Main import main
from PopupMenu import popupMenu
from Menu import menu, obj, button, label, entry, optionBox, listBox, canvas, image
from DmgCalcMenu import dmgCalcMenu
main = main("wiki", "800x500")
characterEditorPopup = popupMenu("menu", "300x150")

dmgCalcMenu = dmgCalcMenu()
menu1 = menu()

dmgCalcMenu.assignIcons({
    "displayCanvas" : canvas([200, 60], [599, 400]),
    "weaponListBox" : listBox([1, 100], [201, 160], lambda *args : dmgCalcMenu.loadWeapon()),
    "attackButton" : button([100, 80], [100, 19], "Start attacking", dmgCalcMenu.startAttacking),
    "menuButton" : button([100, 100], [100, 19], "menu", lambda : characterEditorPopup.activate("")),
})

menu1.assignIcons({
    "b" : button([1, 1], [100, 19], "back", characterEditorPopup.deactivate),   
})

characterEditorPopup.assignMenus([menu1])

main.assignMenus([dmgCalcMenu])
main.activate()

main.root.mainloop()
