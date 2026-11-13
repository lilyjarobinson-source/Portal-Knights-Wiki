from Main import main
from WeaponController import weaponController
from ArmourController import armourController
from CharacterController import characterController

class main(main):
    def __init__(self, title, geometry):
        super().__init__(title, geometry)
        self.weaponController = None
        self.armourController = None
        self.characterController = None

    def initialise(self):
        super().initialise()
        self.weaponController = weaponController()
        self.armourController = armourController()
        self.characterController = characterController(self.weaponController, self.armourController)
