# CF Python Course

This repository contains all exercises, projects, and learning materials completed during the CareerFoundry Python course.  
It documents my progress from foundational Python concepts to building and deploying a full Django web application.

---

## 📂 Repository Structure

- **Achievement 1** – Core Python exercises (data types, loops, functions, OOP basics)  
- **Achievement 2** – Django Recipe App project  
  - `Exercise 2.2` – Initial setup of the Recipe App  
  - `Exercise 2.7` – Search, charts, tests, and documentation  
  - `Exercise 2.8` – Deployment notes and Render setup  
- **Learning Journal** – Notes and reflections on each exercise and milestone  

---

## 🍴 Django Recipe App

The main project in this course is a **Recipe Management Web App** built with Python and Django.

### Features
- Add recipes with **title, author, description, ingredients, instructions, image**
- Extra fields: **prep time, cook time, serves**
- User authentication (register, login, logout)
- Admin panel for managing recipes
- Responsive design with custom CSS
- Deployment on **Render**

### Live Demo
👉 [Django Recipe App on Render](https://django-recipe-app-6t2d.onrender.com)

### Source Code
👉 [Recipe App Repository](https://github.com/sagunanathani/django-recipe-app)

---

## ⚙️ Tech Stack

- **Python 3.11+**
- **Django**
- **HTML, CSS, JavaScript**
- **PostgreSQL (for deployment)**
- **GitHub Actions / CI/CD**
- **Render (deployment)**

---

## 🚀 Getting Started

Clone the repository:
```bash
git clone https://github.com/sagunanathani/cf-python-course.git
cd cf-python-course/Achievement\ 2/Exercise\ 2.2/A2_Recipe_App/src

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


📝 Learning Journal
All reflections, notes, and troubleshooting steps are documented in the Learning Journal folder.
This includes deployment notes, mentor feedback, and personal insights during the course.

🙌 Acknowledgements
Thanks to CareerFoundry mentors and tutors for guidance throughout the course.
Special focus on building clean, maintainable code and professional workflows
