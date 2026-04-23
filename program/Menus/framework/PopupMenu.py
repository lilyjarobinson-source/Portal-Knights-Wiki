from tkinter import *
from Main import main
class popupMenu(main):
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry
        self.active = False
        self.menus = []
        self.currentMenuIndex = -1
        self.currentMenu = None
        self.root = None
        self.theme = {}
        
    def activate(self, root, position, menuIndex):
        self.initialise(root, position)
        self.active = True
        if self.currentMenuIndex != -1:
            self.changeMenu(menuIndex)
        else:
            self.currentMenuIndex = menuIndex
            self.currentMenu = self.menus[self.currentMenuIndex]
            self.reloadMenu()

    def initialise(self, root, position):
        self.root = Toplevel(root)
        self.root.title(self.title)
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
