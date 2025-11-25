- Code Practice 1: Adding Entries
- Recipe App with MySQL (Exercise 1.6 Task)

# 📘 Exercise 1.6 – MySQL Integration

This folder contains two practice tasks demonstrating how to use **Python with MySQL** to store, update, and manage data. Both tasks build on earlier exercises where file handling and object‑oriented programming were used, now extended with database operations.

## 📝 1.6 – Practice Task 1: Adding Entries

### 📌 Overview

In this task, I created a **stock table** in MySQL and added entries using Python’s `mysql.connector`. This helped me practice writing `INSERT` queries and committing changes to the database.

### ✅ Steps Completed

- Connected to MySQL using the `cf-python` user.
- Created a table called `stock` with columns:
  - `id` (INT)
  - `name` (VARCHAR)
  - `manufacturer` (VARCHAR)
  - `price` (FLOAT)
  - `qty` (INT)
- Inserted the following entries:
  - `(4, 'Paper', 'Georgia-Pacific Corp.', 35, 40)`
  - `(5, 'Butter', 'Organic Valley', 18, 37)`
  - `(6, 'Pencils', 'Staedtler', 17, 55)`
- Verified entries using `SELECT * FROM stock`.

### 📸 Deliverables

- Screenshot of table creation.
- Screenshot of `INSERT` queries.
- Screenshot of `SELECT * FROM stock` output showing the new entries.

---

## 📝 1.6 – Task: Recipe App with MySQL

### 📌 Overview

This task extended my Recipe app to use **MySQL for persistent storage**. I built a command‑line program (`recipe_mysql.py`) with a main menu that allows users to add, search, update, and delete recipes.

### ✅ Steps Completed

- Connected Python to MySQL and created a database called `task_database`.
- Created a `Recipes` table with columns:
  - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
  - `name` (VARCHAR(50))
  - `ingredients` (VARCHAR(255)) – stored as comma‑separated strings
  - `cooking_time` (INT)
  - `difficulty` (VARCHAR(20))
- Implemented functions:
  - `create_recipe()` – add new recipes
  - `search_recipe()` – search recipes by ingredient
  - `update_recipe()` – modify recipe details and recalculate difficulty if needed
  - `delete_recipe()` – remove recipes by ID
- Built a `main_menu()` loop to let users interact with the app until they choose to exit.

### 📸 Deliverables

- Screenshot of database and table creation.
- Screenshot of adding recipe.
- Screenshot of searching recipes by ingredient.
- Screenshot of updating recipes (2–3 updates).
- Screenshot of deleting one recipe.
- Screenshot of exiting the program.

## 💬 Reflection

- Learned how to integrate Python with MySQL for real‑world data storage.
- Practiced SQL operations (`CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`) through Python scripts.
- Understood how to handle lists in MySQL by converting them into comma‑separated strings.
- Improved confidence in building command‑line apps with persistent storage.
- Strengthened workflow discipline by organizing deliverables and documenting each step.

## 📖 Summary

This exercise demonstrated how to integrate Python with MySQL for real-world applications.

- In **Practice Task 1**, I created and populated a stock table with sample entries.
- In the **Recipe App Task**, I built a command-line program with CRUD operations on a Recipes table.  
  Through these tasks, I strengthened my understanding of SQL queries, database design, and Python integration.

Completing Exercise 1.6 gave me confidence in bridging Python with relational databases. I now understand how to design tables, store structured data, and build interactive command-line apps with persistent storage. This exercise also taught me the importance of clean documentation and organized GitHub submissions, which I’ll carry forward into future projects.
