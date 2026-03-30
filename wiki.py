import sys
sys.path.append(__file__.split(__file__.split("\\")[-1])[0] + "program-data")
from Main import main
from Menu import menu, obj, button, label, entry, optionBox, listBox, canvas, image
from DmgCalcMenu import dmgCalcMenu
main = main()
dmgCalcMenu = dmgCalcMenu()

dmgCalcMenu.assignIcons({
    "displayCanvas" : canvas([200, 60], [599, 400]),
    "attackButton" : button([100, 80], [100, 19], "Start attacking", dmgCalcMenu.startAttacking)
})

main.assignMenus([dmgCalcMenu])
main.activate(geometry = "800x500", title = "wiki")

main.root.mainloop()
