# Initialize empty lists
recipes_list = []
ingredients_list = []

# step - 1
# Function to take recipe input from user
def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]

    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

# step - 2
# Ask user how many recipes to enter
n = int(input("How many recipes would you like to enter? "))

# Collect recipes
for i in range(n):
    print(f"\n--- Entering recipe {i+1} ---")
    recipe = take_recipe()

    # Add unique ingredients to ingredients_list
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    # Add recipe to recipes_list
    recipes_list.append(recipe)

# # step - 3
# Display all recipes with difficulty
print("\n=== Recipe List ===")
for recipe in recipes_list:
    name = recipe['name']
    time = recipe['cooking_time']
    ingredients = recipe['ingredients']
    num_ingredients = len(ingredients)

    # Determine difficulty
    if time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    # Display recipe
    print(f"\nRecipe: {name}")
    print(f"Cooking Time (min): {time}")
    print(f"Ingredients: {', '.join(ingredients)}")
    print(f"Difficulty: {difficulty}")

# step - 4
# Display all ingredients used
print("\n=== All Ingredients Used ===")
for ingredient in sorted(ingredients_list):
    print(ingredient)