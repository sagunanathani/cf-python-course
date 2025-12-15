# Exercise 2.7 – Recipe App Search & Visualization

## 📄 Task-2.7 Overview
This exercise implements **search functionality** for recipes, integrates **data visualization**, and documents the workflow with tests and execution flow.

---

## 🔍 Search Implementation
- **Criteria**: Users can search by recipe title, description, or ingredients.
- **Wildcard Support**: Partial queries (e.g., "Pasta" → "Pasta al pesto").
- **Show-All Option**: Checkbox to display all recipes without filters.
- **Output Format**: Results displayed in a responsive grid/table with:
  - Recipe image
  - Title
  - Short description
  - Cooking time & servings
  - Clickable link to recipe detail page

---

## 📊 Data Analysis
Three visualizations were implemented using **Matplotlib** and **Pandas**:

1. **Bar Chart – Servings by Recipe**
   - **X-axis**: Recipe titles
   - **Y-axis**: Number of servings
   - **Purpose**: Compare serving sizes across recipes

2. **Pie Chart – Cook Time Distribution**
   - **Labels**: Recipe titles
   - **Values**: Cook time (minutes)
   - **Purpose**: Show percentage share of cook times

3. **Line Chart – Prep Time by Recipe**
   - **X-axis**: Recipe titles (sorted alphabetically)
   - **Y-axis**: Prep time (minutes)
   - **Purpose**: Visualize prep time trends

Charts are displayed **directly below search results**.

---

## 🧪 Testing
- **Form Tests**: Validate required fields, lengths, and formats.
- **View Tests**: Ensure login protection, correct search filtering, pagination.
- **Execution**:
  ```bash
  python manage.py test -v 2