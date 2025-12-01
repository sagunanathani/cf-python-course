# 📘 Exercise 1.7 – Practice Task 3

## 🎯 Objective

Practice updating entries in the `practice_recipes` table using SQLAlchemy ORM.

## 🛠️ Steps Taken

1. Retrieved the Cake recipe object using `get()`:

   ```python
   cake = session.query(Recipe).get(4)
   or
   cake = session.query(Recipe).filter(Recipe.name == "Cake").one()

   ```

2. Appended a new ingredient:

# Check current ingredients

print(cake.ingredients)

# Append new ingredient

cake.ingredients += ", Chocolate Powder"

# Show updated ingredients (without committing yet)

print(cake.ingredients)

3. Verified the updated ingredient list in IPython

Step 3: (Optional) Commit Changes
For this practice, you don’t need to commit. But if you wanted to persist the change:
session.commit()

📊 Output
Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk, Chocolate Powder

✅ Alternative: Direct Update with update()
If want to change directly in the database without loading the object:

session.query(Recipe).filter(Recipe.name == "Cake").update({
Recipe.ingredients: "Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk, Chocolate Powder"
})
session.commit()

👉 In short:

- IPython → shows the update in your Python object.
- MySQL CLI → shows the update persisted in the database after session.commit().
