# 📘 Exercise 1.7 – SQLAlchemy ORM Practice & Final Recipe App

## 🎯 Objective

This exercise focused on learning and practicing SQLAlchemy ORM operations in Python, gradually building towards a complete command-line Recipe application.  
The tasks covered **reading, filtering, updating, deleting entries**, and finally creating a **full CRUD Recipe app**.

---

## 🛠️ Task 1: Reading Entries from a Table

- Used `session.query(Recipe).all()` to retrieve all recipes as Python objects.
- Accessed attributes with dot notation (`recipe.id`, `recipe.name`, etc.).
- Printed recipes using a loop and the `__str__` method.
- Verified results matched the database entries.

📸 Screenshots:

- Code retrieving all recipes.
- Output showing Tea, Coffee, Cake, Banana Smoothie.

---

## 🛠️ Task 2: Filtering Entries

- Practiced using `filter()` with `like()` to search for recipes containing **Sugar**.
- Example:

  ```python
  recipes_with_sugar = session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%")).all()

  - Displayed results with a loop, confirming multiple recipes matched.

  📸 Screenshots:
  ```

- Code using filter() with like("%Sugar%").
- Output showing Tea, Coffee, Cake, Banana Smoothie.

---

## 🛠️ Task 3: Updating Entries

- Retrieved Cake recipe using get() or filter().one().
- Appended Chocolate Powder to its ingredients:
  cake.ingredients += ", Chocolate Powder"
  print(cake.ingredients)

- Verified updated ingredients string in Python (no commit required for practice).

  📸 Screenshots:

- Code editing Cake’s ingredients.
- Output showing updated ingredient list.

---

## 🛠️ Task 4: Deleting Entries

- Added a temporary recipe Buttered Toast.
- Retrieved it with:
  recipe_to_delete = session.query(Recipe).filter(Recipe.name == "Buttered Toast").one()
  - Deleted using:
    session.delete(recipe_to_delete)
    session.commit()
- Verified deletion by querying names only:
  session.query(Recipe.name).all()

  📸 Screenshots:

- Adding Buttered Toast.
- Deleting Buttered Toast.
- Output showing remaining recipes.

---

## 🛠️ Final Task: Recipe App

Built a complete command-line Recipe app (recipe_app.py) with full CRUD functionality.
Features

- Create a new recipe
  - Collects name, ingredients, cooking time.
  - Validates inputs.
  - Calculates difficulty automatically.
  - Saves to database.
- View all recipes
  - Retrieves all recipes.
  - Displays formatted details using **str**.
  - Search by ingredients
  - Lists all unique ingredients.
  - Allows user to select one or more.
  - Filters recipes using like() conditions.
- Edit a recipe
  - User selects recipe by ID.
  - Can edit name, ingredients, or cooking time.
  - Difficulty recalculated automatically.
- Delete a recipe
  - User selects recipe by ID.
  - Confirms deletion before committing.
- Quit application

  - Closes session and engine gracefully.

  Menu Loop
  --- Recipe App Menu ---

1. Create a new recipe
2. View all recipes
3. Search for recipes by ingredients
4. Edit a recipe
5. Delete a recipe
   Type 'quit' to exit

📸 Screenshots:

- Creating recipes.
- Viewing recipes.
- Searching by ingredients.
- Editing a recipe.
- Deleting a recipe.
- Exiting the app.

📂 Folder Structure

Exercise 1.7/
│
├── 1.7-Practice Task 1/ # Reading entries
├── 1.7-Practice Task 2/ # Filtering entries
├── 1.7-Practice Task 3/ # Updating entries
├── 1.7-Practice Task 4/ # Deleting entries
├── Final Task/ # Full Recipe app
│ ├── recipe_app.py
│ ├── screenshots/
│ └── README.md
└── README.md # This summary file

## 📝 Reflection

This exercise demonstrated:

- How SQLAlchemy ORM simplifies database operations compared to raw SQL.
- Importance of input validation and difficulty calculation logic.
- Full CRUD functionality integrated into a user-friendly command-line app.
- Professional workflow: code, screenshots, documentation, and GitHub organization.

👉 This README gives you a **complete overview** of Exercise 1.7, covering **Tasks 1–4** and the **Final Task**.
