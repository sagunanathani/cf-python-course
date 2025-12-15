# 🧠 Learning Journal – Exercise 2.7: Recipe App Search & Visualization

## 📌 Overview
In this exercise I extended the Recipe App with a **search feature** and integrated **data visualization**. I also documented my thought process in *Task‑2.7*, wrote tests for forms and views, and captured the execution flow with screenshots.

---

## 🛠️ What I Did
- Created a **search form** allowing users to:
  - Enter keywords for recipe title, description, or ingredients.
  - Use wildcards/partial queries (e.g., “Pasta” → “Pasta al pesto”).
  - Select a “Show All” option to list all recipes.
- Implemented a **search view**:
  - Extracted data as a QuerySet.
  - Converted results into a **pandas DataFrame**.
  - Displayed results in a responsive grid/table with clickable links to recipe detail pages.
- Added **data visualization** directly below search results:
  - **Bar chart**: Servings by Recipe.
  - **Pie chart**: Cook Time Distribution.
  - **Line chart**: Prep Time by Recipe.
- Wrote **tests**:
  - Checked form fields for values, formats, and lengths.
  - Verified login protection of views.
  - Confirmed search returns correct results and pagination works.
- Ran tests with verbosity set to 2 and saved the outcome screenshot as `test-outcome.jpg`.
- Documented the **execution flow** in Task‑2.7 with a flow chart and screenshots of the user journey.

---

## ✅ What I Learned
- How to design a **user-friendly search interface** with Django forms and views.
- The importance of **wildcard queries** (`icontains`) to make search flexible.
- How to use **pandas** for converting QuerySets into DataFrames for analysis.
- How to integrate **Matplotlib charts** into Django templates using base64 encoding.
- The value of **tests** for ensuring reliability of forms and views.
- How to clearly document the **execution flow** so mentors can follow the user journey step by step.

---

## 📸 Deliverables
- `Task-2.7` document with:
  - Search criteria notes
  - Data Analysis section
  - Execution flow chart
  - Screenshots of user journey
- `screenshots/test-outcome.jpg` → test results
- `user-journey.mp4` screencast
- Updated Recipe App code in GitHub repository

---

## 💬 Reflection
This exercise helped me connect multiple skills: **search logic, data analysis, visualization, and testing**. I now understand how to make search results more meaningful by adding charts and ensuring everything is tested and documented. It also reinforced the importance of presenting my work professionally with journals, screenshots, and GitHub uploads.  

I feel more confident in building **interactive, data-driven Django applications** that combine backend logic with frontend visualization.