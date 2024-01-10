'''Design a recipe management system with classes for recipes, ingredients, and
users. Implement methods for adding recipes, searching by ingredients'''

class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, name, ingredients, instructions, user):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.user = user

    def display_info(self):
        print(f"\nRecipe: {self.name}")
        print(f"Ingredients: {', '.join(ingredient.name for ingredient in self.ingredients)}")
        print(f"Instructions: {self.instructions}")
        print(f"User: {self.user.name}")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name.lower() == ingredient_name.lower():
                    matching_recipes.append(recipe)
                    break
        return matching_recipes

# Example usage:
ingredient1 = Ingredient("Paneer")
ingredient2 = Ingredient("Rice")
ingredient3 = Ingredient("Tomatoes")

user1 = User(1, "John Doe")
user2 = User(2, "Jane Smith")

recipe1 = Recipe("Paneer Curry", [ingredient1, ingredient2, ingredient3], "Cook and enjoy!", user1)
recipe2 = Recipe("Vegetable Stir Fry", [ingredient2, ingredient3], "Stir-fry veggies and enjoy!", user2)
recipe3 = Recipe("Tomato Rice", [ingredient2, ingredient3], "Make rice with tomatoes!", user1)

recipe_manager = RecipeManager()
recipe_manager.add_recipe(recipe1)
recipe_manager.add_recipe(recipe2)
recipe_manager.add_recipe(recipe3)

# Search for recipes with a specific ingredient
ingredient_to_search = input("Enter an ingredient to search for: ")
matching_recipes = recipe_manager.search_by_ingredient(ingredient_to_search)

if matching_recipes:
    print(f"\nRecipes containing {ingredient_to_search}:")
    for recipe in matching_recipes:
        recipe.display_info()
else:
    print(f"\nNo recipes found containing {ingredient_to_search}.")
