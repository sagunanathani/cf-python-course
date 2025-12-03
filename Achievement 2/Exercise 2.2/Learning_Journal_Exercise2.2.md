📝 Learning Journal – Exercise 2.2

🎯 Objective

To create and deploy a Django project named recipe_project inside a structured folder A2_Recipe_App, and document the setup process with screenshots and GitHub submission.

✅ Steps Completed

1. Created Folder Structure

   - Created A2_Recipe_App directory.
   - Initialized virtual environment a2-ve-recipeapp and activated it.

2. Installed Django

   - Used pip to install Django inside the virtual environment.

3. Created Django Project

   - Ran django-admin startproject recipe_project inside A2_Recipe_App.
   - Captured screenshot: proj_contents_before_renaming.jpg

4. Renamed Project Directory

   - Renamed recipe_project to src.
   - Captured screenshot: proj_contents_after_renaming.jpg

5. Ran Migrations and Server

   - Executed python manage.py migrate inside src.
   - Ran python manage.py runserver.
   - Captured browser success page: success_message.jpg

6. Created Superuser and Logged into Admin

   - Used python manage.py createsuperuser.
   - Logged into Django admin via browser.
   - Captured dashboard screenshot: admin-dashboard.jpg

7. GitHub Submission
   - Created Exercise 2.2 folder inside Achievement 2 repo.
   - Uploaded A2_Recipe_App folder.
   - Created screenshots subfolder and uploaded all images.
   - Uploaded updated learning journal.

📂 GitHub Folder Structure

Achievement 2/
└── Exercise 2.2/
├── A2_Recipe_App/
└── screenshots/
├── proj_contents_before_renaming.jpg
├── proj_contents_after_renaming.jpg
├── success_message.jpg
└── admin-dashboard.jpg

🧠 Reflections - Learned how Django projects are structured and deployed locally. - Understood the difference between project and app. - Practiced using manage.py for migrations, server, and superuser creation. - Gained confidence in organizing and documenting a full Django setup.
