🧠 Learning Journal – Exercise 1.5: Recipe App with OOP
📌 Overview
In this exercise, I refactored my Recipe Manager application to use object-oriented programming (OOP) principles. Instead of storing recipes as dictionaries, I created a Recipe class with attributes and methods to encapsulate recipe data and behavior. This made the code more modular, reusable, and easier to extend.

🛠️ What I Did

- Defined a Recipe class with attributes:
- name, ingredients, cooking_time, and difficulty
- A class variable all_ingredients to track unique ingredients across all recipes

- Implemented methods:
- **init**() for initialization
- Getter and setter methods for name and cooking_time
- add_ingredients() to add multiple ingredients and update the global list
- calculate_difficulty() to determine difficulty based on cooking time and number of ingredients
- search_ingredient() to check if a recipe contains a specific ingredient
- update_all_ingredients() to maintain the class-level ingredient list
- **str**() for a formatted string representation of each recipe
- Created a helper function recipe_search() to search across multiple recipes by ingredient.
- Built and tested four recipe objects:
- Tea (Tea Leaves, Sugar, Water; 5 minutes)
- Coffee (Coffee Powder, Sugar, Water; 5 minutes)
- Cake (Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk; 50 minutes)
- Banana Smoothie (Bananas, Milk, Peanut Butter, Sugar, Ice Cubes; 5 minutes)

- Grouped recipes into a list and searched for recipes containing Water, Sugar, and Bananas.
- Added print checkpoints to mark steps for screenshots:
- Steps1-5_RecipeCreation.png → recipe creation and display
- Steps6-7_RecipeSearch.png → ingredient search results

✅ What I Learned

- How to design and implement a Python class with attributes and methods.
- The importance of encapsulation: keeping recipe data and behavior together in one object.
- How class variables can track shared data across multiple objects.
- How OOP makes the code more concise compared to procedural dictionary-based approaches.
- How to use **str**() for clean, user-friendly output.
- How to structure code for easier debugging and documentation (print checkpoints for screenshots).

📸 Deliverables

- recipe_oop.py script file
- Screenshots:
- Steps1-5_RecipeCreation.png
- Steps6-7_RecipeSearch.png
- Updated Learning Journal entry (this file)

💬 Reflection
This task helped me transition from procedural programming to object-oriented programming in Python. By encapsulating recipe data and logic inside a class, the application became more organized and scalable. I can now easily add new features (like saving recipes to files or editing them) without rewriting large parts of the code. The use of class variables and methods also gave me a better understanding of how OOP supports reusability and maintainability.
I feel more confident applying OOP principles to future projects, and this exercise reinforced the importance of clean design and documentation in professional development workflows.
