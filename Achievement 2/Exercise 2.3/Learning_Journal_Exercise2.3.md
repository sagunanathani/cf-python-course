# 🧠 Learning Journal – Exercise 2.3: Recipe App Schema & Admin

## 📌 Overview

In this exercise, I extended my Django project by designing a database schema for recipes and ingredients, creating new apps, defining models, and registering them in the admin panel. I also tested migrations and added sample data to verify functionality.

---

## 🛠️ What I Did

- Designed a **schema diagram** showing the relationship between `Recipe` and `Ingredient` (many-to-many).
- Created two Django apps:
  - `recipes` → stores recipe details (name, description, cooking time, difficulty).
  - `ingredients` → stores individual ingredients.
- Defined models with proper fields and relationships.
- Registered models in the Django admin for easy management.
- Ran `makemigrations` and `migrate` to apply schema changes.
- Wrote simple unit tests to confirm model creation and relationships.
- Added at least five recipes via the admin panel:
  - Tea
  - Coffee
  - Cake
  - Banana Smoothie
  - Pasta
- Captured screenshots of:
  - Schema diagram
  - Project structure
  - Migration commands
  - Admin panel with recipes and ingredients

---

## ✅ What I Learned

- How to design a relational schema in Django using **Many-to-Many relationships**.
- The importance of separating entities into different apps for modularity.
- How migrations track changes in models and update the database schema.
- How to use the Django admin panel to quickly add and manage data.
- The difference between storing ingredients as strings vs. normalized objects in a separate table.

---

## 📸 Deliverables

- `schema_diagram.png` → shows Recipe ↔ Ingredient relationship.
- `project_structure.png` → updated folder layout with apps.
- `migrations_screenshot.png` → proof of migrations applied.
- `tests_screenshot.png` → unit test results.
- `recipes_list.png` → five recipes added in admin panel.
- `Learning_Journal_Exercise2.3.md` → this file.

---

## 💬 Reflection

This task helped me move from a simple Django setup (Exercise 2.2) to a structured application with multiple apps and a normalized schema. By separating recipes and ingredients, I learned how Django handles complex relationships and how the admin panel simplifies data entry.

I feel more confident about designing scalable applications in Django, and this exercise reinforced the importance of schema planning, migrations, and testing. It also showed me how documentation and screenshots provide clear evidence of progress for mentors and reviewers.
