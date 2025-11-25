📘 Learning Journal – Exercise 1.6 (Recipe App with MySQL)
✅ What I Did

- Installed and configured MySQL Connector for Python using python -m pip install mysql-connector-python.
- Connected Python to MySQL with the cf-python user and verified the connection.
- Created a new database (task_database) and switched to it using USE task_database.
- Designed and created a Recipes table with columns for id, name, ingredients, cooking_time, and difficulty.
- Implemented a main menu loop in recipe_mysql.py with options to:
- Add new recipes
- Search recipes by ingredient
- Update existing recipes
- Delete recipes
- Exit the program
- Added logic to calculate recipe difficulty based on cooking time and number of ingredients.
- Practiced inserting recipes, searching by ingredient, updating values, and deleting entries.
- Organized deliverables into GitHub folders (Exercise 1.6-Task) with screenshots and code.

✅ Key Learnings

- Database Integration: Learned how to connect Python scripts to MySQL and execute SQL queries directly from Python.
- Data Types: Understood the difference between Python data structures and MySQL column types (e.g., using VARCHAR, INT, FLOAT).
- Ingredients Handling: Since MySQL doesn’t support arrays, I stored ingredients as comma-separated strings and used .split() and .join() to convert between lists and strings.
- SQL Operations: Practiced CREATE DATABASE, CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE queries through Python’s cursor.execute().
- Error Handling: Encountered issues like “cursor not connected” and solved them by reinitializing the connection and cursor.
- Workflow Discipline: Captured screenshots at each step, grouped them neatly, and documented the process for submission.

✅ Reflections

- I now feel confident in combining object-oriented programming with database management.
- The main menu loop taught me how to structure user interactions in a command-line app.
- Debugging connection errors improved my troubleshooting skills and patience.
- This exercise showed me how professional applications store and manage data beyond simple file handling.
- I’m proud of how I organized my GitHub repo with clear folders, filenames, and documentation — it reflects professional standards.

✅ Next Steps

- Expand the Recipe app with more advanced queries (e.g., filtering by cooking time or difficulty).
- Explore foreign keys and relationships between tables for more complex data models.
- Practice writing more reusable functions and modular code for database operations.
- Continue refining my GitHub portfolio with polished documentation and screenshots.
