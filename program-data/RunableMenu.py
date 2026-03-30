from Menu import menu
class runableMenu(menu):
    running = False
    runable = True
    root = None
    
    def activate(self, root, theme):
        self.root = root
        self.theme = theme
        for i in list(self.icons.values()):
            i.activate(root, theme)
        self.initialise(root)
        self.run()
        
    def deactivate(self):
        self.running = False
        for i in list(self.icons.values()):
            i.deactivate()
        self.unitialise()

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.root.update()

    def update(self):
        pass
