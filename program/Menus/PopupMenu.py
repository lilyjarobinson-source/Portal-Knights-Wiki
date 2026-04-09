from tkinter import *
from Main import main
class popupMenu(main):
    title = ""
    geometry = ""
    active = False
        
    def activate(self, position):
        self.initialise(position)
        self.active = True
        self.currentMenu = self.menus[self.currentMenuIndex]
        self.reloadMenu()


    def initialise(self, position):
        self.root = Tk()
        self.root.geometry(self.geometry)

    def deactivate(self):
        if self.active:
            self.currentMenu.deactivate()
            self.root.destroy()
            self.active = False

    def isPopupMenuClosedFunction(self):
        return True
