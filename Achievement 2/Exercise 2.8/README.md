# Exercise 2.8 – Deploying a Django Application

## 🔧 Static Files (CSS & JavaScript)
- Django treats CSS, JS, and images as **static files**.  
- Place them inside the `static/` directory of your app or project.  
- Use `{% load static %}` in templates and reference with `<link>` or `<script>` tags.  
- During deployment, run `collectstatic` to gather all static files into one location for serving in production.

---

## 🚀 Deployment Steps
1. **Prepare Project**
   - Set `DEBUG=False` in `settings.py`.
   - Generate a new `SECRET_KEY`.
   - Configure `ALLOWED_HOSTS`.
   - Update `requirements.txt` (include `gunicorn`).

2. **Local Test**
   - Run app with production settings.
   - Confirm static files load correctly.

3. **Push to GitHub**
   - Commit all changes.
   - Ensure `render.yaml` (or equivalent config) is included.

4. **Deploy on Render**
   - Create a new Web Service.
   - Set build/start commands:
     - `pip install -r requirements.txt`
     - `python manage.py migrate`
     - `python manage.py collectstatic --noinput`
     - `gunicorn recipe_project.wsgi`
   - Add environment variables (`SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`).

5. **Verify**
   - Test login/logout, recipe list, search.
   - Check HTTPS and security headers.
   - Confirm static/media files are served.

---

## 📝 Reflection

### ✅ What went well
- Clear structure and hands-on exercises.  
- Balanced theory + practice made learning smooth.  
- Gained confidence working with Python and Django.

### 🌟 What I’m proud of
- Successfully deploying a real Django app.  
- The sense of accomplishment when seeing the app live.  
- Building something useful and professional.

### ⚡ Challenges
- Adapting deployment steps to Render instead of Heroku.  
- Understanding production settings and environment variables.  
- Required independence and experimentation, which was valuable.

### 🎯 Expectations
- Achievement met expectations fully.  
- Now confident to start Django projects.  
- Already exploring a real-world project with Angular + Django.

---

## 📂 Deliverables
- Screenshot of test results saved as:  
  `Achievement 2/Exercise 2.8/screenshots/test-report.jpg`

---

## ✅ Completion
This exercise demonstrates the full cycle:  
**develop → test → deploy → verify → reflect**.  
With this, Achievement 2 is complete, and the Django journey continues 🚀.