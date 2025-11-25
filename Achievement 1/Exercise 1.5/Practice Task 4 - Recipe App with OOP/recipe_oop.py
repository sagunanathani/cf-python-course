class Recipe:
    # Class variable to track all ingredients across recipes
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    # --- Getter and Setter for name ---
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # --- Getter and Setter for cooking_time ---
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, time):
        # Safeguard cooking time input
        if not isinstance(time, (int, float)) or time < 0:
            raise ValueError("Cooking time must be a positive number.")
        self.cooking_time = time
        self.calculate_difficulty()

    # --- Add ingredients ---
    def add_ingredients(self, *args):
        for ingredient in args:
            # Normalize ingredients to lowercase
            self.ingredients.append(ingredient.lower())
        self.update_all_ingredients()
        self.calculate_difficulty()

    def get_ingredients(self):
        return self.ingredients

    # --- Difficulty calculation ---
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    # --- Ingredient search ---
    def search_ingredient(self, ingredient):
        # Normalize search term to lowercase
        return ingredient.lower() in self.ingredients

    # --- Update class variable ---
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # --- String representation ---
    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.get_difficulty()}\n")

    # --- Static method for recipe search ---
    @staticmethod
    def recipe_search(data, search_term):
        print(f"\nSearching for recipes with ingredient: {search_term}")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)


# --- Script Execution ---
if __name__ == "__main__":
    print("=== Step 1: Create Tea Recipe Object ===")
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)
    print(tea)

    print("=== Step 2: Create Coffee Recipe Object ===")
    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)
    print(coffee)

    print("=== Step 3: Create Cake Recipe Object ===")
    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    cake.set_cooking_time(50)
    print(cake)

    print("=== Step 4: Create Banana Smoothie Recipe Object ===")
    smoothie = Recipe("Banana Smoothie")
    smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    smoothie.set_cooking_time(5)
    print(smoothie)

    recipes_list = [tea, coffee, cake, smoothie]

    print("=== Step 5: Search Recipes with Ingredient 'Water' ===")
    Recipe.recipe_search(recipes_list, "Water")

    print("=== Step 6: Search Recipes with Ingredient 'Sugar' ===")
    Recipe.recipe_search(recipes_list, "Sugar")

    print("=== Step 7: Search Recipes with Ingredient 'Bananas' ===")
    Recipe.recipe_search(recipes_list, "Bananas")


