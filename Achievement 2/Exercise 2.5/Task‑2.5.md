# 📘 Exercise 2.5 – Recipe App Development

This document records the steps and decisions made while completing **Exercise 2.5** of the CF Python course.

---

## 1. Model Updates

### Models from Exercise 2.3
- **Recipe**
  - `title` (CharField, max_length=100)
  - `author_name` (CharField, max_length=50)
  - `description` (TextField)
  - `ingredients` (TextField, stored as line‑separated list)
  - `instructions` (TextField)
  - `prep_time` (IntegerField)
  - `cook_time` (IntegerField)
  - `serves` (IntegerField)
  - `difficulty` (CharField, calculated and stored)
  - `image` (ImageField, upload to `static/images/`)

### Changes Made
- ✅ **No structural changes** were required compared to Exercise 2.3.  
- The `difficulty` attribute is retained but recalculated dynamically in the detail view (based on prep + cook time and number of ingredients, as practiced in Achievement 1).  
- Added `description` field to improve recipe overview cards.  
- All other attributes remain unchanged.

---

## 2. Records Added

At least **five recipes** were entered via the Django Admin panel:

Images for each recipe were downloaded and stored locally in `static/images/`.

---

## 3. Welcome Page

- Designed a **hero section** with a full‑screen background image (`bg-food.jpg`).
- Added overlay text: *“Welcome to Our Recipes Home”* with a button linking to the overview page.
- Footer fixed at the bottom of the page.
- Inspiration sources documented in `journal.doc` under *Frontend Inspirations*.

📸 Screenshot saved as: `welcome.jpg`

---

## 4. Recipes Overview Page

- Displays all recipes in a **grid layout** with cards.
- Each card shows image, title, author, prep/cook times, and a “View Details” button.
- Heading styled with orange theme and decorative underline.

📸 Screenshot saved as: `recipes-overview.jpg`

---

## 5. Recipe Details Page

- Displays full recipe information: title, meta info, image, ingredients, instructions.
- Difficulty calculated dynamically and displayed.
- Styled with consistent orange theme (matching overview page).
- Includes a “Back to Overview” button.

📸 Screenshots saved as:  
- `recipe1.jpg` 

---

## 6. Tests

- Verified that:
  - All links between pages work.
  - Recipes load correctly from the database.
  - Difficulty calculation logic matches Achievement 1.
- All tests passed successfully.

📸 Screenshots saved as:  
- `test_pass_recipes.jpg` 
---

## 7. GitHub Deliverables

- **Achievement‑2 Repository**
  - `Exercise-2.5/Task-2.5.md`
  - `Exercise-2.5/Screenshots/`  
    - `welcome.jpg`  
    - `recipes-overview.jpg`  
    - `recipe1.jpg`  
    - `test_pass_recipes.jpg` etc...

- **Recipe App Repository**
  - Updated Django project code in `src/`.

---

## 💬 Reflection

- Learned how to connect models, admin entries, and templates into a cohesive app.  
- Practiced modular CSS and consistent theming across pages.  
- Improved confidence in designing professional layouts with Django template inheritance.  
- Reinforced workflow discipline by documenting changes and organizing deliverables in GitHub.

---