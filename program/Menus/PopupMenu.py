from tkinter import *
from Main import main
class popupMenu(main):
    title = ""
    geometry = ""
        
    def activate(self, position):
        self.initialise(position)
        self.loadTheme()
        self.currentMenu = self.menus[self.currentMenuIndex]
        self.currentMenu.activate(self.root, self.theme)

    def initialise(self, position):
        self.root = Tk()
        self.root.geometry(self.geometry)

    def deactivate(self):
        self.currentMenu.deactivate()
        self.root.destroy()
