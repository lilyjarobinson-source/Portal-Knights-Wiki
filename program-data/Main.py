from tkinter import *
hexDigits = "0123456789abcdef"

class main:
    def __init__(self):
        self.menus = []
        self.currentMenuIndex = 0
        self.currentMenu = None
        self.root = None
        self.theme = {}

    def initialise(self, kwargs):
        self.root = Tk()
        if "geometry" in kwargs:
            self.root.geometry(kwargs["geometry"])
        else:
            self.root.geometry("200x200")
        if "title" in kwargs:
            self.root.title(kwargs["title"])
        else:
            self.root.title("Main")

    def assignMenus(self, menus):
        self.menus = menus

    def setMapMenuIndex(self, index):
        self.mapMenuIndex = index

    def activate(self, **kwargs):
        self.initialise(kwargs)
        self.loadTheme()
        self.currentMenu = self.menus[self.currentMenuIndex]
        self.currentMenu.activate(self.root, self.theme)

    def reloadMenu(self):
        self.loadTheme()
        self.currentMenu.deactivate()
        self.currentMenu.activate(self.root, self.theme)

    def changeMenu(self, targetIndex):
        self.loadTheme()
        self.menus[self.currentMenuIndex].deactivate()
        self.currentMenuIndex = targetIndex
        self.currentMenu = self.menus[targetIndex]
        self.currentMenu.activate(self.root, self.theme)

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
            if i.lower() not in hexDigits:
                notHex = True
                break
        if not notHex:
            colour = "#" + colour
        self.root.config(bg=colour)
