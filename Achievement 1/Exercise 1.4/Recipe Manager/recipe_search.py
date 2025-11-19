import pickle

def display_recipe(recipe):
    print("\n📖 Recipe Details")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(f"{index}: {ingredient}")
    try:
        choice = int(input("Pick an ingredient by number: "))
        ingredient_searched = data["all_ingredients"][choice]
    except (ValueError, IndexError):
        print("Invalid selection.")
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)

filename = input("Enter recipe data filename: ")

try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found.")
else:
    search_ingredient(data)