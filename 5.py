# Create a Bus child class that inherits from the Vehicle class. The default fare
# charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we
# need to add an extra 10% on full fare as a maintenance charge. So total fare for
# bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        # Default fare calculation: seating capacity * 100
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        # Inherit the default fare calculation from the Vehicle class
        default_fare = super().calculate_fare()

        # Add an extra 10% on the full fare for maintenance charge
        maintenance_charge = 0.1 * default_fare

        # Calculate the total fare for Bus instance
        total_fare = default_fare + maintenance_charge

        return total_fare

# Taking user input to create a Bus instance
seating_capacity = int(input("Enter the seating capacity of the bus: "))
bus_instance = Bus(capacity=seating_capacity)

# Calculate and display the total fare
bus_fare = bus_instance.calculate_fare()
print(f"The total fare for the bus with a seating capacity of {bus_instance.capacity} is ${bus_fare:.2f}.")
