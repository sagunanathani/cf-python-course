    
# -------------------------------
# Imports
# -------------------------------
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

#  virtual environment: cf-python-base
# -------------------------------
# Load environment variables
# -------------------------------
# this will read from .env file
load_dotenv(override=True)  # ensures .env values replace system ones

USERNAME = os.getenv("USERNAME") # MySQL username
PASSWORD = os.getenv("PASSWORD") # MySQL password
HOST = os.getenv("HOST")         # usually localhost
DB_NAME = os.getenv("DB_NAME") # database created earlier

# -------------------------------
# Database Connection
# -------------------------------

engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# -------------------------------
# Recipe Model
# -------------------------------
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} ({self.difficulty})>"

    def __str__(self):
        return (
            "\n" + "-"*40 + "\n"
            + f"Recipe ID:\t{self.id}\n"
            + f"Name:\t\t{self.name}\n"
            + f"Ingredients:\t{self.ingredients}\n"
            + f"Cooking Time:\t{self.cooking_time} minutes\n"
            + f"Difficulty:\t{self.difficulty}\n"
            + "-"*40
        )

    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return [i.strip().lower() for i in self.ingredients.split(",")]

    def set_cooking_time(self, time):
        if not isinstance(time, (int, float)) or time < 0:
            raise ValueError("Cooking time must be a positive number.")
        self.cooking_time = int(time)
        self.calculate_difficulty()

    @staticmethod
    def recipe_search(data, search_term):
        return [r for r in data if search_term.lower() in r.ingredients.lower()]

# -------------------------------
# Create Table
# -------------------------------
Base.metadata.create_all(engine)

# -------------------------------
# Functions
# -------------------------------
def create_recipe():
    print("\n--- Create a New Recipe ---")
    name = input("Enter recipe name: ").strip()
    if len(name) > 50:
        print("❌ Name too long (max 50 characters).")
        return

    while True:
        try:
            cooking_time = int(input("Enter cooking time (minutes): "))
            break
        except ValueError:
            print("❌ Please enter a valid number for cooking time.")

    while True:
        try:
            num_ingredients = int(input("How many ingredients? "))
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    ingredients_set = set()
    for i in range(num_ingredients):
        ing = input(f"Enter ingredient {i+1}: ").strip().lower()
        ingredients_set.add(ing)

    ingredients_str = ", ".join(sorted(ingredients_set))

    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    print("✅ Recipe added successfully!")


def view_all_recipes():
    print("\n--- View All Recipes ---")
    recipes = session.query(Recipe).all()
    if not recipes:
        print("❌ No recipes found in the database.")
        return
    for recipe in recipes:
        print(recipe)


def search_by_ingredients():
    print("\n--- Search by Ingredients ---")
    if session.query(Recipe).count() == 0:
        print("❌ No recipes found.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = set()
    for row in results:
        for ing in row[0].split(", "):
            all_ingredients.add(ing.lower())

    all_ingredients = sorted(all_ingredients)
    print("\nAvailable Ingredients:")
    for idx, ing in enumerate(all_ingredients):
        print(f"{idx}: {ing}")

    choice = input("Enter ingredient numbers (space-separated): ").split()
    try:
        choice = [int(c) for c in choice]
    except ValueError:
        print("❌ Invalid input.")
        return

    if any(c < 0 or c >= len(all_ingredients) for c in choice):
        print("❌ Invalid ingredient selection.")
        return

    search_ingredients = [all_ingredients[c] for c in choice]
    conditions = [Recipe.ingredients.like(f"%{ing}%") for ing in search_ingredients]

    recipes = session.query(Recipe).filter(*conditions).all()
    if not recipes:
        print("❌ No recipes found with those ingredients.")
    else:
        for recipe in recipes:
            print(recipe)


def edit_recipe():
    print("\n--- Edit a Recipe ---")
    recipes = session.query(Recipe.id, Recipe.name).all()
    if not recipes:
        print("❌ No recipes found.")
        return

    for r in recipes:
        print(f"{r.id}: {r.name}")

    try:
        recipe_id = int(input("Enter recipe ID to edit: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    recipe_to_edit = session.query(Recipe).get(recipe_id)
    if not recipe_to_edit:
        print("❌ Recipe not found.")
        return

    print("\n1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")
    choice = input("Which attribute would you like to edit? ")

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        recipe_to_edit.name = new_name
    elif choice == "2":
        new_ing = input("Enter new ingredients (comma-separated): ").strip().lower()
        recipe_to_edit.ingredients = new_ing
    elif choice == "3":
        while True:
            try:
                new_time = int(input("Enter new cooking time: "))
                recipe_to_edit.set_cooking_time(new_time)
                break
            except ValueError:
                print("❌ Cooking time must be a positive number.")
    else:
        print("❌ Invalid choice.")
        return

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("✅ Recipe updated successfully!")


def delete_recipe():
    print("\n--- Delete a Recipe ---")
    recipes = session.query(Recipe.id, Recipe.name).all()
    if not recipes:
        print("❌ No recipes found.")
        return

    for r in recipes:
        print(f"{r.id}: {r.name}")

    try:
        recipe_id = int(input("Enter recipe ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    recipe_to_delete = session.query(Recipe).get(recipe_id)
    if not recipe_to_delete:
        print("❌ Recipe not found.")
        return

    confirm = input(f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ").lower()
    if confirm == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("✅ Recipe deleted successfully!")
    else:
        print("❌ Deletion cancelled.")

# -------------------------------
# Main Menu
# -------------------------------
def main_menu():
    while True:
        print("\n--- Recipe App Menu ---")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("Closing application...")
            session.close()
            engine.dispose()
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

