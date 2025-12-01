# 📘 Exercise 1.7 – Practice Task 2

## 🎯 Objective

Practice using SQLAlchemy’s **`filter()`** method to retrieve specific entries from the `practice_recipes` table.  
In this task, the goal was to query all recipes that contain **Sugar** in their ingredients list.

---

## 🛠️ Steps Taken

1. **Opened IPython** inside the `cf-python-base` environment.
2. **Queried the database** using the ORM `filter()` method with `like("%Sugar%")`.

   ```python
   from sqlalchemy import text
   from sqlalchemy import or_
   recipes_with_sugar = session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%")).all()

   ```

3. Iterated through results and printed details for each recipe:
   for recipe in recipes_with_sugar:
   print("Recipe ID:", recipe.id)
   print("Recipe Name:", recipe.name)
   print("Ingredients:", recipe.ingredients)
   print("Cooking Time:", recipe.cooking_time)
   print("Difficulty:", recipe.difficulty)
   print("-" \* 40)

4. Verified that all recipes containing "Sugar" were retrieved successfully

📊 OutputThe query returned the following recipes:

Recipe ID: 1
Recipe Name: Tea
Ingredients: Tea Leaves, Water, Sugar
Cooking Time: 5
Difficulty: None

---

Recipe ID: 3
Recipe Name: Coffee
Ingredients: Coffee Powder, Sugar, Water
Cooking Time: 5
Difficulty: None

---

Recipe ID: 4
Recipe Name: Cake
Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
Cooking Time: 50
Difficulty: None

---

Recipe ID: 5
Recipe Name: Banana Smoothie
Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Cooking Time: 5
Difficulty: None

---

👉 In short:

- IPython → shows the update in your Python object.
- MySQL CLI → shows the update persisted in the database after session.commit().
