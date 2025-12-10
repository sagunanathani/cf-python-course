🍳 Recipe App

Recipe App is a simple web application built with Python and Django.
It allows users to view, add, and manage recipes while demonstrating Django’s core features such as models, migrations, testing, and admin integration.

🚀 Features
Create and store recipes in an SQLite database
Each recipe includes a name, list of ingredients, cooking time, and difficulty rating
Automatically assign difficulty level based on cooking time
Manage recipes through the Django Admin dashboard
Basic automated tests for model fields and methods

🧱 Tech Stack
Backend: Django 5.x
Language: Python 3.x
Database: SQLite (default)

⚙️ Installation & Setup
1. Clone the repository:
git clone https://github.com/LambicJaune/recipe_app.git
cd recipe_app

2. Create and activate a virtual environment:
(a2-ve-recipeapp) PS C:\Users\Saguna Nathani\Desktop\CF_Projects\cf-python-course> 
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver

6. Access the app: Open your browser and go to http://localhost:8000

🧪 Running Tests
To run automated tests for the app:
python manage.py test

👩‍💻 Author
Developed by Saguna Nathani 


📘 Updated README – Exercise 2.2 & 2.3

Project Title

A2_Recipe_App – Django Setup, Schema Design, and Recipe Management

# Recipe App

This Django application allows users to create, view, and search recipes by ingredients.
Recipes include cooking time, difficulty, and descriptions.
The app uses a relational schema with Recipes and Ingredients linked via Many-to-Many relationships.

Description:

This project demonstrates the setup and development of a Django application named recipe_project, renamed to src, with full deployment steps including migrations, server run, superuser creation, and admin access.
In Exercise 2.3, the application was extended to include a Recipe management system with schema design, app creation, model registration, testing, and data entry via the admin panel.

Folder Structure

- A2_Recipe_App/ – Contains the Django project.
- screenshots/ – Contains setup screenshots.
- Exercise 2.3/ – Contains schema diagram, project structure, migration and test screenshots, and recipe data screenshots
- learning_journal.md – Reflective journal of the task.

Setup Instructions

1. Clone the repo.
2. Navigate to A2_Recipe_App.
3. Activate virtual environment. (a2-ve-recipeapp)
4. Run python manage.py migrate.
5. Run python manage.py runserver.
6. Access via http://127.0.0.1:8000/
7. Log in to admin panel and manage recipes

Features Added in Exercise 2.3

- Database schema design for Recipe and Ingredient entities
- Created Django apps: recipes and ingredients
- Defined models and registered them in admin
- Ran migrations and added unit tests
- Entered five sample recipes via admin panel
- Documented all steps with screenshots

Author
Saguna Nathani
