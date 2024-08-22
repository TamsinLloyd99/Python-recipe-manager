import json
import os

# Class to represent a Recipe
class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['ingredients'], data['instructions'])


# Global constant for the filename where recipes are stored
DATA_FILE = 'recipes.json'

def load_recipes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Recipe.from_dict(item) for item in data]
    else:
        return []
    
def save_recipes(recipes):
    with open(DATA_FILE, 'w') as f:
        json.dump([recipe.to_dict() for recipe in recipes], f , indent=4)

def add_recipe(recipe):
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)

def view_recipes():
    recipes = load_recipes()
    for recipe in recipes:
        print(f"Title: {recipe['title']}")
        print(f"Ingredients: {', '.join(recipe.ingredients)}")
        print(f"Instructions: {recipe.instructions}")
        print()

def search_recipes(query):
    recipes = load_recipes()
    results = []
    for recipe in recipes:
        if query.lower() in recipe.title.lower() or any(query.lower() in ingredient.lower() for ingredient in recipe.ingredients):
            results.append(recipe)
    return results

def edit_recipe(title, new_title=None, new_ingredients=None, new_instructions=None):
    recipes = load_recipes()
    for recipe in recipes:
        if recipe.title == title:
            if new_title:
                recipe.title = new_title
            if new_ingredients:
                recipe.ingredients = new_ingredients
            if new_instructions:
                recipe.instructions = new_instructions
            break
    save_recipes(recipes)

def delete_recipe(title):
    recipes = load_recipes()
    recipes = [recipe for recipe in recipes if recipe.title != title]
    save_recipes(recipes)

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nRecipe Manager")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_new_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_for_recipe()
        elif choice == '4':
            edit_existing_recipe()
        elif choice == '5':
            delete_existing_recipe()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def add_new_recipe():
    """Handle adding a new recipe."""
    title = input("Enter the recipe title: ").strip()
    ingredients = input("Enter the ingredients (comma separated): ").strip().split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    instructions = input("Enter the instructions (comma separated): ").strip()

    new_recipe = Recipe(title, ingredients, instructions)
    add_recipe(new_recipe)
    print(f"Recipe '{title}' added successfully!")

def view_all_recipes():
    """Handle viewing all recipes."""
    recipes = load_recipes()
    if recipes:
        for recipe in recipes:
            print(f"Title: {recipe.title}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print(f"Instructions: {recipe.instructions}")
            print("-" * 20)
    else:
        print("No recipes found.")

def search_for_recipe():
    """Handle searching for a recipe by title or ingredient."""
    query = input("Enter a title or ingredient to search: ").strip()
    results = search_recipes(query)
    if results:
        for recipe in results:
            print(f"Title: {recipe.title}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print(f"Instructions: {recipe.instructions}")
            print("-" * 20)
    else:
        print(f"No recipes found matching '{query}'.")

def edit_existing_recipe():
    """Handle editing an existing recipe."""
    title = input("Enter the title of the recipe to edit: ").strip()
    recipes = load_recipes()
    for recipe in recipes:
        if recipe.title == title:
            new_title = input(f"Enter new title (leave blank to keep '{recipe.title}'): ").strip()
            new_ingredients = input("Enter new ingredients (comma separated, leave blank to keep current): ").strip()
            new_instructions = input("Enter new instructions (leave blank to keep current): ").strip()

            new_title = new_title if new_title else recipe.title
            new_ingredients = [ing.strip() for ing in new_ingredients.split(',')] if new_ingredients else recipe.ingredients
            new_instructions = new_instructions if new_instructions else recipe.instructions

            edit_recipe(recipe.title, new_title, new_ingredients, new_instructions)
            print(f"Recipe '{title}' updated successfully!")
            return
    print(f"Recipe '{title}' not found.")

def delete_existing_recipe():
    """Handle deleting an existing recipe."""
    title = input("Enter the title of the recipe to delete: ").strip()
    delete_recipe(title)
    print(f"Recipe '{title}' deleted successfully!")

# If the script is being run directly, start the main menu
if __name__ == "__main__":
    main_menu()



# 9. Project Presentation:
# Prepare a brief presentation demonstrating your Recipe Manager.
# Showcase the functionalities and explain how they were implemented.
# Discuss any challenges faced during the development process and how you overcame them.

# 10. Submission:
# Submit your project files along with any necessary documentation.
# Include instructions on how to run the Recipe Manager.

