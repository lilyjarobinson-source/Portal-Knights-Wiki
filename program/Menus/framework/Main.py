from tkinter import *
class main:
    hexDigits = "0123456789abcdef"
    
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry
        self.popupMenus = []
        self.currentPopupMenuIndex = -1
        self.menus = []
        self.currentMenuIndex = -1
        self.currentMenu = None
        self.menuWasRunning = False
        self.root = None
        self.theme = {}
        self.poppedUpMenu = False
        self.popupMenuHasJustClosed = False

    def initialise(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.bind('<Button-1>', lambda event : self.raisePopupOnFocus())

    def assignMenus(self, menus):
        self.menus = menus

    def addMenus(self, menus):
        self.menus += menus
        
    def assignPopupMenus(self, popupMenus):
        self.popupMenus = popupMenus

    def activate(self):
        self.initialise()
        self.currentMenuIndex = 0
        self.currentMenu = self.menus[self.currentMenuIndex]
        self.reloadMenu()

    def reloadMenu(self):
        self.loadTheme()
        self.currentMenu.deactivate()
        self.currentMenu.activate(self.root, self.theme, self.isPopupMenuClosedFunction)

    def changeMenu(self, targetIndex):
        self.loadTheme()
        self.currentMenu.deactivate()
        self.currentMenuIndex = targetIndex
        self.currentMenu = self.menus[targetIndex]
        self.currentMenu.activate(self.root, self.theme, self.isPopupMenuClosedFunction)

    def loadTheme(self):
        try:
            file = open("SELECTEDTHEMELOCATION", "r")
            theme = file.read()
            file.close()
            
            file = open("THEMELOCATION", "r")
            content = file.read()
            file.close()
            
            self.theme = {
                "name" : "",
                "bg" : "",
                "buttonBg" : "",
                "buttonTx" : "",
                "labelBg" : "",
                "labelTx" : "",
                "entryBg" : "",
                "entryTx" : "",
                "optionBoxBg" : "",
                "optionBoxTx" : "",
                "listBoxBg" : "",
                "listBoxTx" : "",
                "canvasBg" : "",
                "canvasTx" : "",
            }
            
            content = content.split("\n")
            keys = list(self.theme.keys())
            for i in range(len(content)):
                self.theme[keys[i]] = content[i]
        except:
            self.theme = {
                "name" : "default",
                "bg" : "SystemButtonFace",
                "buttonBg" : "#e0e0e0",
                "buttonTx" : "#000000",
                "labelBg" : "SystemButtonFace",
                "labelTx" : "#000000",
                "entryBg" : "#ffffff",
                "entryTx" : "#000000",
                "optionBoxBg" : "SystemButtonFace",
                "optionBoxTx" : "#000000",
                "listBoxBg" : "#ffffff",
                "listBoxTx" : "#000000",
                "canvasBg" : "#ffffff",
                "canvasTx" : "#000000",
            }
        self.changeBgColour(self.theme["bg"])

    def changeBgColour(self, colour):
        notHex = False
        for i in colour:
            if i.lower() not in self.hexDigits:
                notHex = True
                break
        if not notHex:
            colour = "#" + colour
        self.root.config(bg=colour)

    def popUpMenu(self, index, menuIndex):
        self.currentPopupMenuIndex = index
        if self.isPopupMenuClosedFunction():
            #'''
            if self.currentMenu.running:
                self.menuWasRunning = True
                self.currentMenu.stopRunning()
            #'''
            self.popupMenus[index].activate(self.root, "", menuIndex)
            self.poppedUpMenu = True
            self.popupMenus[self.currentPopupMenuIndex].root.wm_attributes("-topmost", True)

    def popDownMenu(self):
        if self.poppedUpMenu:
            self.popupMenuHasJustClosed = True
            self.poppedUpMenu = False
            self.popupMenus[self.currentPopupMenuIndex].deactivate()
            self.currentPopupMenuIndex = -1

    def raisePopupOnFocus(self):
        self.isPopupMenuClosedFunction()
        if self.popupMenuHasJustClosed:
            self.popupMenuHasJustClosed = False
            self.onPopupClosure()

    def onPopupClosure(self):
        self.currentMenu.reload(self.root)
        if self.menuWasRunning:
            self.menuWasRunning = False
            self.currentMenu.startRunning()

    def isPopupMenuClosedFunction(self):
        if self.poppedUpMenu:
            try:
                if self.popupMenus[self.currentPopupMenuIndex].root.winfo_exists():
                    self.popupMenus[self.currentPopupMenuIndex].active = True
                else:
                    self.popDownMenu()
            except:
                self.popDownMenu()
        else:
            self.popDownMenu()
        return not self.popupMenus[self.currentPopupMenuIndex].active

        
    
