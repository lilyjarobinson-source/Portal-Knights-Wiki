import sys
sys.path.append(__file__.split(__file__.split("\\")[-1])[0] + "Menus")
from Main import main
from Menu import menu, obj, button, label, entry, optionBox, listBox, canvas, image
from DmgCalcMenu import dmgCalcMenu
main = main()
dmgCalcMenu = dmgCalcMenu()

dmgCalcMenu.assignIcons({
    "weaponListBox" : listBox([1, 100], [201, 160], lambda *args : dmgCalcMenu.loadWeapon()),
    "displayCanvas" : canvas([203, 60], [596, 400]),
    "attackButton" : button([102, 80], [100, 19], "Start attacking", dmgCalcMenu.startAttacking)
})

main.assignMenus([dmgCalcMenu])
main.activate(geometry = "800x500", title = "wiki")

main.root.mainloop()
