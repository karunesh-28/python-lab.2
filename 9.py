'''Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Add
methods and attributes specific to each subclass.'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # Placeholder method, to be overridden by subclasses


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def scratch_furniture(self):
        return f"{self.name} is scratching the furniture."


# Taking user input to create a Dog object
dog_name = input("Enter the dog's name: ")
dog_age = input("Enter the dog's age: ")
dog_breed = input("Enter the dog's breed: ")

# Creating a Dog object
dog_object = Dog(dog_name, dog_age, dog_breed)

# Displaying details and specific features of the Dog
print(f"\nDog Details: {dog_object.name}, {dog_object.age} years old, Breed: {dog_object.breed}")
print(f"Sound: {dog_object.make_sound()}")
print(dog_object.fetch())

# Taking user input to create a Cat object
cat_name = input("\nEnter the cat's name: ")
cat_age = input("Enter the cat's age: ")
cat_color = input("Enter the cat's color: ")

# Creating a Cat object
cat_object = Cat(cat_name, cat_age, cat_color)

# Displaying details and specific features of the Cat
print(f"\nCat Details: {cat_object.name}, {cat_object.age} years old, Color: {cat_object.color}")
print(f"Sound: {cat_object.make_sound()}")
print(cat_object.scratch_furniture())
