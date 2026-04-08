import random, time
from tkinter import *
hexDigits = "0123456789abcdef"


class menu:
    icons = {}
    theme = {}
    runable = False
    running = False
    root = None
    isPopupMenuClosedFunction = None

    def __init__(self, runable=False):
        self.runable = runable
    
    def activate(self, root, theme, isPopupMenuClosedFunction):
        self.root = root
        self.theme = theme
        self.isPopupMenuClosedFunction = isPopupMenuClosedFunction
        for i in list(self.icons.values()):
            i.activate(root, theme, self.isPopupMenuClosedFunction)
        self.initialise(root)
        if self.runable:
            self.run()

    def assignIcons(self, icons):
        self.icons = icons

    def activateIcon(self, iconName):
        self.icons[iconName].activate(root)
        
    def deactivateIcon(self, iconName):
        self.icons[iconName].deactivate()

    def deactivate(self):
        self.running = False
        for i in list(self.icons.values()):
            i.deactivate()
        self.unitialise()

    def initialise(self, root):
        pass
    
    def unitialise(self):
        pass

    def reload(self):
        pass

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.root.update()

    def update(self):
        pass
    

class obj:
    isPopupMenuClosedFunction = None
    def __init__(self, pos, dimensions):
        self.pos = pos
        self.obj = None
        self.dimensions = dimensions
        self.active = False
        self.colour = ""
        self.border = ""

    def activate(self, root, theme, isPopupMenuClosedFunction):
        if not self.active:
            self.setColour(theme)
            self.initialise(root)
            self.active = True
            self.isPopupMenuClosedFunction = isPopupMenuClosedFunction
        
    def deactivate(self):
        if self.active:
            self.active = False
            self.obj.destroy()

    def initialise(self, root):
        pass

    def place(self, pos=None, dimensions=None):
        if pos != None:
            self.pos = pos.copy()
        if dimensions != None:
            self.dimensions = dimensions.copy()
        self.obj.place(x=self.pos[0], y=self.pos[1], width=self.dimensions[0], height=self.dimensions[1])

    def raiseObj(self):
        self.obj.tkraise()

    def setColour(self, theme):
        colour = theme[self.name + "Bg"]
        notHex = False
        for i in colour:
            if i.lower() not in hexDigits:
                notHex = True
                break
        if not notHex:
            colour = "#" + colour
        self.colour = colour
        
        colour = theme[self.name + "Tx"]
        notHex = False
        for i in colour:
            if i.lower() not in hexDigits:
                notHex = True
                break
        if not notHex:
            colour = "#" + colour
        self.textColour = colour

    def updateBgColour(self, colour):
        self.obj.config(bg=colour)
        
    def updateTxColour(self, colour):
        self.obj.config(fg=colour)
        

class button(obj):
    name = "button"
    colour = "#e0e0e0"
    textColour = "#000000"
    def __init__(self, pos, dimensions, text, command):
        super().__init__(pos, dimensions)
        self.text = text
        self.fun = command

    def initialise(self, root):
        self.obj = Button(root, text=self.text, command=self.checkForPopUpMenu, borderwidth=1, relief="solid", bg=self.colour, fg=self.textColour)
        self.place()

    def checkForPopUpMenu(self):
        if self.isPopupMenuClosedFunction():
            self.fun()

    def set(self, text):
        self.text = text
        self.obj.config(text=text)

    def get(self):
        return self.text

    def clear(self):
        self.text = ""

class label(obj):
    name = "label"
    colour = "SystemButtonFace"
    textColour = "#000000"
    def __init__(self, pos, dimensions, text, textAlign="c"):
        super().__init__(pos, dimensions)
        self.text = text
        self.textAlign = textAlign
        match textAlign:
            case "w":
                self.textJustify = "left"
            case "e":
                self.textJustify = "right"
            case _:
                self.textJustify = "center"
                

    def initialise(self, root):
        self.obj = Label(root, text=self.text, borderwidth=1, relief="solid", bg=self.colour, fg=self.textColour, anchor=self.textAlign, justify=self.textJustify)
        self.place()
        
    def set(self, text):
        self.text = text
        self.obj.config(text=self.text)

    def get(self):
        return self.text

    def clear(self):
        self.text = ""
        self.obj.config(text=self.text)

class entry(obj):
    name = "entry"
    colour = "#000000"
    textColour = "#000000"
    contents = None
    fun = None
    def __init__(self, pos, dimensions):
        super().__init__(pos, dimensions)

    def initialise(self, root):
        self.obj = Entry(root, textvariable=self.contents, borderwidth=1, relief="solid", bg=self.colour, fg=self.textColour)
        if self.contents == None:
            self.contents = StringVar()
        self.place()

    def get(self):
        return self.contents.get()

    def set(self, contents):
        self.contents.set(contents)
        self.obj.config(textvariable=self.contents)

    def clear(self):
        self.contents.set("")
        self.obj.config(textvariable=self.contents)

    def bindFunctionToKeypress(self, fun):
        self.fun = fun
        self.obj.bind("<KeyRelease>", self.checkForPopUpMenu)

    def checkForPopUpMenu(self):
        if self.isPopupMenuClosedFunction():
            self.fun()

class optionBox(obj):
    name = "optionBox"
    colour = "SystemButtonFace"
    textColour = "#000000"
    defaultOption = None
    selectedOption = None
    fun = None
    def __init__(self, pos, dimensions, options, selectedOption):
        super().__init__(pos, dimensions)
        self.options = options
        self.defaultOption = selectedOption
    
    def initialise(self, root):
        if self.selectedOption == None:
            self.selectedOption = StringVar(value=self.defaultOption)
        else:
            self.setSelectedOption(self.defaultOption)
        self.obj = OptionMenu(root, self.selectedOption, *self.options)
        self.obj.config(bg=self.colour, borderwidth=1, relief="solid", highlightthickness=0, fg=self.textColour)
        self.place()

    def get(self):
        return self.selectedOption.get()

    def setSelectedOption(self, option):
        self.selectedOption.set(option)

    def setOptions(self, root, theme, options):
        self.options = options
        self.deactivate()
        self.activate(root, theme)

    def bindFunctionToKeypress(self, fun):
        self.fun = fun
        self.selectedOption.trace_add("write", fun)

    def checkForPopUpMenu(self):
        if self.isPopupMenuClosedFunction():
            self.fun()

class listBox(obj):
    name = "listBox"
    colour = "#000000"
    textColour = "#000000"
    def __init__(self, pos, dimensions, command):
        super().__init__(pos, dimensions)
        self.items = []
        self.fun = command

    def initialise(self, root):
        self.obj = Listbox(root, borderwidth=1, relief="solid", bg=self.colour, highlightthickness=0, fg=self.textColour)
        self.clear()
        self.obj.bind("<<ListboxSelect>>", self.checkForPopUpMenu)
        self.place()

    def checkForPopUpMenu(self):
        if self.isPopupMenuClosedFunction():
            self.fun()

    def getIndex(self):
        return self.obj.curselection()

    def getValue(self):
        index = self.obj.curselection()
        if len(index) > 0:
            index = index[0]
            return self.items[index]

    def getItems(self):
        return self.items.copy()

    def insert(self, index, item):
        self.items.insert(index, item)
        self.obj.insert(index, item)

    def append(self, item):
        self.items.append(item)
        self.obj.insert(len(self.items)-1, item)

    def delete(self, index):
        self.items.pop(index)
        self.obj.delete(index)

    def clear(self):
        self.items = []
        self.obj.delete(0, END)

    def getItemFromIndex(self, index):
        return self.items[index]

class canvas(obj):
    name = "canvas"
    colour = "#ffffff"
    textColour = "#000000"
    def initialise(self, root):
        self.obj = Canvas(root, borderwidth=1, relief="solid", bg=self.colour, highlightthickness=0)
        self.place()

    def dot(self, x, y):
        self.obj.create_oval(x-3, y-3, x+3, y+3, fill="black")

    def line(self, x1, y1, x2, y2, arrow="none"):
        self.obj.create_line(x1, y1, x2, y2, arrow=arrow)

    def image(self, x, y, image, anchor="center"):
        self.obj.create_image(x, y, image=image, anchor=anchor)
        
    def write(self, x, y, text, anchor="center"):
        self.obj.create_text(x, y, text=text, fill=self.textColour, anchor=anchor)

    def clear(self):
        self.obj.delete("all")

class image(obj):
    name = "label"
    colour = "SystemButtonFace"
    textColour = "#000000"
    def __init__(self, pos, dimensions, image=None):
        super().__init__(pos, dimensions)
        self.image = image
                
    def initialise(self, root):
        if self.image == None:
            self.obj = Label(root, text="image", borderwidth=1, relief="solid", bg=self.colour, fg=self.textColour)
        else:
            self.obj = Label(root, image=self.image, borderwidth=1, relief="solid")
        self.place()
        
    def set(self, image):
        if self.image == None:
            self.obj.config(text="")
        self.image = image
        self.obj.config(image=self.image)
