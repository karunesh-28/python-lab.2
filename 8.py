'''Create a Python class called “Car” with attributes like make, model, and year.
Then, create an object of the “Car” class and print its details.'''
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} -  {self.name} - {self.model}")

# Taking user input to create a Car object
name = input("Enter the car's name: ")
model = input("Enter the car's model: ")
year = input("Enter the car's year: ")

# Creating a Car object
car_object = Car(name, model, year)

# Displaying the details of the Car object
car_object.display_details()
