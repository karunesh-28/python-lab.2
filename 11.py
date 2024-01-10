'''Create a base class called “Vehicle” with a method called “drive.” Implement two
subclasses, “Car” and “Bicycle,” that inherit from “Vehicle” and override the “drive”
method with their own implementations.'''

class Vehicle:
    def drive(self):
        print("Generic Vehicle - Driving")

class Car(Vehicle):
    def drive(self):
        print("Car - Driving")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle - Riding")

# Example usage:
vehicle = Vehicle()
car = Car()
bicycle = Bicycle()

# Calling the drive method for each object
print("Vehicle:")
vehicle.drive()

print("\nCar:")
car.drive()

print("\nBicycle:")
bicycle.drive()
