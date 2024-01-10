'''Define a class attribute “color” with a default value white. i.e., Every Vehicle
should be white.'''
class Vehicle:
    # Class attribute with default value 'white'
    color = 'white'

    def __init__(self, model):
        self.model = model

    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")


# Taking user input for color
user_input_color = input("Enter the color of the vehicle (press Enter for default white): ").strip()

# Creating an instance of the Vehicle class
if user_input_color:
    # If user provides a color, set it for the instance
    vehicle_instance = Vehicle(model="Vahanam")
    vehicle_instance.color = user_input_color
else:
    # Use the default white color
    vehicle_instance = Vehicle(model="Vahanam")

# Displaying information about the vehicle
vehicle_instance.display_info()
