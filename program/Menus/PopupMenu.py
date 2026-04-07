from Main import main
class popupMenu(main):
    title = ""
    geometry = ""
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry
        
    def activate(self, position):
        self.initialise()
        self.loadTheme()
        self.currentMenu = self.menus[self.currentMenuIndex]
        self.currentMenu.activate(self.root, self.theme)

    def initialise(self, position):
        self.root = Tk()
        self.root.geometry(self.geometry)
