# Recipe App – Authentication Feature

## 📖 Project Overview
This project extends the Recipe App by adding **user authentication**. The goal was to implement a secure login/logout flow, protect certain views, and provide a polished user experience with clear navigation.

---

## 🚀 Features Implemented

### 1. Login
- Created a **login view** in `views.py` using Django’s built-in authentication system.
- Built a **login template** (`login.html`) with a styled form and error handling.
- Registered the login view in `urls.py` at `/login/`.
- Added a **login link** on the homepage (`base.html`) that routes directly to the login form.

### 2. Protected Views
- Identified sensitive pages (e.g., `records` page).
- Added `@login_required` decorators to these views.
- Verified that unauthenticated users are redirected to `/login/`.

### 3. Logout
- Added a **logout link** on protected pages.
- Created a **logout view** in `views.py` using `django.contrib.auth.logout`.
- Built a **success.html** template with:
  - Message: *“You’ve successfully logged out.”*
  - Links to log back in and browse recipes.
  - Creative touch: background image and styled buttons.

### 4. User Journey
- Homepage → Login → Authentication form → Redirect to protected page → Logout → Success page.

---

## 🛠️ How to Run Locally

1. Navigate to the project folder:
   ```bash
   cd A2_Recipe_App/src

2. Activate the virtual environment:
    source ../a2-ve-recipeapp/bin/activate   # Mac/Linux
    a2-ve-recipeapp\Scripts\activate        # Windows

3. Run the server:
    python manage.py runserver

4. Open in browser:
    http://127.0.0.1:8000/

🎥 Screencast
A screencast was recorded to demonstrate the full user journey:
- Landing on homepage
- Clicking login
- Entering credentials
- Redirect to protected page
- Logging out
- Success page with creative design
(Video uploaded separately as part of submission)


