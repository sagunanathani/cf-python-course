# 📘 Exercise 2.3 – Recipe App Schema & Admin

## Project Title

**django-recipe-app** – Django Schema Design, Migrations, and Recipe Management

## Description

This exercise extends the Django project created in Exercise 2.2.  
The project demonstrates:

- Designing a relational schema for recipes and ingredients.
- Creating separate Django apps (`recipes` and `ingredients`).
- Defining models and registering them in the admin panel.
- Running migrations and unit tests.
- Adding sample recipes via the admin interface.
- Documenting all steps with screenshots and reflections.

---

## Folder Structure

- `Exercise 2.3/`
  - `schema_diagram.png` – Database schema design
  - `project_structure.png` – Updated Django project layout
  - `migrations_screenshot.png` – Proof of migrations applied
  - `tests_screenshot.png` – Unit test results
  - `recipes_list.png` – Admin panel showing five recipes
  - `Learning_Journal_Exercise2.3.md` – Reflective journal
  - `README.md` – This file

---

## Setup Instructions

1. Clone the `django-recipe-app` repository:

   ```bash
   git clone https://github.com/Saguna Nathani/django-recipe-app.git

   ```

2. Navigate to the project folder:
   cd django-recipe-app

3. Create and activate a virtual environment: a2-ve-recipeapp
   python -m venv venv
   source venv/bin/activate # Mac/Linux
   venv\Scripts\activate # Windows

4. Install dependencies:
   pip install -r requirements.txt

5. Run migrations:
   python manage.py migrate

6. Start the server:
   python manage.py runserver

7. Access the app at http://127.0.0.1:8000/

8. Log in to the admin panel (/admin) to manage recipes and ingredients.

Features

- 📝 Add, edit, and delete recipes via the Django admin panel.
- 🍳 Manage ingredients as separate entities linked to recipes.
- 🔍 Search recipes by ingredients.
- ✅ Unit tests for models to ensure reliability.
- 📂 Clean project structure with modular apps.

Author
Saguna Nathani
