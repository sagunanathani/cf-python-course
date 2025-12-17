# 🍳 Recipe App

A comprehensive Django-based web application for managing and discovering recipes.  
Users can browse, search, add, and analyze recipes with an intuitive interface and powerful filtering capabilities.

🌐 Live Demo: [Recipe App on render](https://django-recipe-app-6t2d.onrender.com)

---

## 🚀 Features

### 📖 Recipe Management
- Create and store recipes in an SQLite database
- Each recipe includes:
  - Name
  - Ingredients
  - Cooking time
  - Difficulty rating (auto-assigned based on cooking time)
  - Description
  - Recipe images
- Browse all available recipes
- View detailed recipe information
- Add new recipes to the database
- Like/favorite recipes
- Manage recipes through the Django Admin dashboard

### 🔍 Advanced Search & Filtering
- Search recipes by:
  - Name
  - Ingredients
  - Difficulty level (Easy, Medium, Hard, Expert)
  - Maximum cooking time
- Paginated results for better navigation
- Visual data analysis with charts:
  - Bar chart: Recipe cooking times
  - Pie chart: Difficulty distribution
  - Line chart: Cooking time trends

### 📊 Data Analysis
- Statistical visualization using Matplotlib
- Interactive charts for recipe analysis
- Pandas DataFrame integration for data processing

### 🧪 Testing
- Basic automated tests for model fields and methods
- Unit tests for schema and relationships

---

## 🧱 Tech Stack
- **Framework:** Django 4.x / 5.x
- **Language:** Python 3.x
- **Database:** SQLite (default)
- **Data Analysis:** Pandas, Matplotlib
- **Frontend:** HTML5, CSS3
- **Pagination:** Django Paginator

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/sagunanathani/Recipe-App.git
   cd Recipe-App

2. Create and activate a virtual environment
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies
    pip install -r requirements.txt

4. Set up the database
    python manage.py makemigrations
    python manage.py migrate

5. Create a superuser (admin account)
    python manage.py createsuperuser

6. Collect static files
    python manage.py collectstatic

7. Run the development server
    python manage.py runserver

8. Access the application
    • 	App: http://127.0.0.1:8000/
    • 	Admin panel: http://127.0.0.1:8000/admin/

📘 Usage
For Regular Users
- Register/Login: Create a new account or log in with existing credentials
- Browse Recipes: View all recipes on the homepage, see popular recipes based on likes
- Search Recipes: Filter by name, ingredients, difficulty, or cooking time
- View Recipe Details: See complete information including ingredients, cooking method, and metadata
- Add Recipes: Share your own recipes with the community
- Like Recipes: Mark recipes as favorites

For Administrators
- Access the admin panel at /admin/
- Manage users, recipes, and all database entries
- Moderate user-submitted content

📂 Folder Structure
- A2_Recipe_App/ – Contains the Django project
- screenshots/ – Setup and feature screenshots
- Exercise 2.3/ – Schema diagram, project structure, migrations, tests, and recipe data screenshots
- learning_journal.md – Reflective journal of the task

Recipe_App/
├── recipe\_app/      # Project app
├── recipes/         # Recipe app containing Recipe model, views, static files, charts
├── users/           # Handles user profiles, authentication, and favourites
├── media/           # Stores uploaded media (profile pictures, recipe images, etc.)
├── templates/       # Global templates (base.html, auth/, registration/)
├── manage.py        # Django management script
├── db.sqlite3       # SQLite database
└── ...

🔧 Configuration
Environment Variables
Create a .env file in the project root for sensitive information:
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=your-database-url

🤝 Contributing
- Fork the repository
- Create a feature branch
git checkout -b feature/AmazingFeature
- Commit your changes
git commit -m 'Add some AmazingFeature'
- Push to the branch
git push origin feature/AmazingFeature
- Open a Pull Request

👩‍💻 Author
Developed by Saguna Nathani
Made with ❤️ and Python


