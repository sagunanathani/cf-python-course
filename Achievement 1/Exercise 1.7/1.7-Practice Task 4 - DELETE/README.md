# 📘 Exercise 1.7 – Practice Task 4

## 🎯 Objective

Practice deleting entries from the `practice_recipes` table using SQLAlchemy ORM.

---

## 🛠️ Steps Taken

1. Added a temporary recipe:

   ```python
   buttered_toast = Recipe(name="Buttered Toast", ingredients="Bread, Butter", cooking_time=4)
   session.add(buttered_toast)
   session.commit()

   ```

2. Retrieved the recipe object by name:
   recipe_to_be_deleted = session.query(Recipe).filter(Recipe.name == "Buttered Toast").one()

3. Deleted the recipe and committed:
   session.delete(recipe_to_be_deleted)
   session.commit()

4. Verified deletion by querying names only
   session.query(Recipe.name).all()

📊 Output
[('Tea'), ('Coffee'), ('Birthday Cake'), ('Banana Smoothie')]

Uploaded in:
Exercise 1.7/1.7-Practice Task 4/

- Adding Buttered Toast
- Retrieving the recipe object
- Deleting the recipe
- Query results showing deletion
