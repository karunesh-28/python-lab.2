'''Implement a class inheritance as following:            
class Shoe:
# Attributes: self.color, self. brand
class Converse (Shoe): # Inherits from Shoe
# Attributes: self.lowOrHighTop, self. tongueColor, self. brand =
class CombatBoot (Shoe): # Inherits from Shoe
# Attributes: self.militaryBranch, self.DesertOrJungle
class Sandal (Shoe): # Inherits from Shoe
# Attributes: self.openOrClosedToe, self.waterproof
You can use any real-world object except a shoe for this problem :)'''

class WoodenStatue:
    def __init__(self, material, size):
        self.material = material
        self.size = size

    def display_info(self):
        print(f"Material: {self.material}, Size: {self.size}")


class KrishnaStatue(WoodenStatue):
    def __init__(self, material, size, flute):
        super().__init__(material, size)
        self.flute = flute

    def display_info(self):
        super().display_info()
        print(f"Flute: {self.flute}")


class RadhaKrishnaStatue(KrishnaStatue):
    def __init__(self, material, size, flute, dress_color):
        super().__init__(material, size, flute)
        self.dress_color = dress_color

    def display_info(self):
        super().display_info()
        print(f"Dress Color: {self.dress_color}")


# Taking user input for Krishna statue details
material_input = input("Enter the material of the statue: ").strip()
size_input = input("Enter the size of the statue: ").strip()
flute_input = input("Does the Krishna statue have a flute? ").strip().capitalize()

# Creating an instance of the RadhaKrishnaStatue class
statue_instance = RadhaKrishnaStatue(material=material_input, size=size_input, flute=flute_input, dress_color="Multi-color")

# Displaying information about the Krishna statue
statue_instance.display_info()
