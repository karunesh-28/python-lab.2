from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob should be in the format 'YYYY-MM-DD'

    def calculate_age(self):
        # Get the current date
        current_date = datetime.now()

        # Extract year, month, and day from the date of birth
        dob_year, dob_month, dob_day = map(int, self.dob.split('-'))

        # Extract year, month, and day from the current date
        current_year, current_month, current_day = current_date.year, current_date.month, current_date.day

        # Calculate the age
        age = current_year - dob_year - ((current_month, current_day) < (dob_month, dob_day))

        return age

# Taking user input to create Person instances
name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
dob = input("Enter the person's date of birth (YYYY-MM-DD): ")

# Creating a Person instance
person = Person(name, country, dob)

# Calculating and displaying the person's age
age = person.calculate_age()
print(f"{person.name} is {age} years old.")
