from tkinter import *
from Main import main
class popupMenu(main):
    title = ""
    geometry = ""
    active = False
        
    def activate(self, position, menuIndex):
        self.initialise(position)
        self.active = True
        if self.currentMenuIndex != -1:
            self.changeMenu(menuIndex)
        else:
            self.currentMenuIndex = menuIndex
            self.currentMenu = self.menus[self.currentMenuIndex]
            self.loadTheme()
            self.currentMenu.activate(self.root, self.theme, self.isPopupMenuClosedFunction)

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

    def setInactive(self):
        self.active = False
        if self.currentMenuIndex != -1:
            for i in self.currentMenu.icons.values():
                i.active = False
