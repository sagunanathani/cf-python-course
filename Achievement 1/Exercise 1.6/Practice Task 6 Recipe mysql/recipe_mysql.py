# Part 1: Create & Connect Database

import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Create Recipes table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

# Part 2: Difficulty Calculator

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# Part 3: Creating a Recipe with create_recipe()

def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    ingredients = [i.strip() for i in ingredients]

    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)

    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, ingredients_str, cooking_time, difficulty))
    conn.commit()
    print("Recipe added successfully!")

# Part 4: Searching for a Recipe with search_recipe()

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = []
    for row in results:
        for ingredient in row[0].split(", "):
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("Available ingredients:")
    for i, ing in enumerate(all_ingredients, 1):
        print(f"{i}. {ing}")

    choice = int(input("Pick an ingredient number: "))
    search_ingredient = all_ingredients[choice - 1]

    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ("%" + search_ingredient + "%",))
    results = cursor.fetchall()

    for recipe in results:
        print(recipe)

# Part 5: Updating a Recipe with update_recipe()

def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for recipe in results:
        print(recipe)

    recipe_id = int(input("Enter recipe ID to update: "))
    column = input("Which column to update (name, cooking_time, ingredients): ")

    new_value = input("Enter new value: ")

    if column == "cooking_time":
        new_value = int(new_value)
        cursor.execute("SELECT ingredients FROM Recipes WHERE id=%s", (recipe_id,))
        ingredients = cursor.fetchone()[0].split(", ")
        difficulty = calculate_difficulty(new_value, ingredients)
        cursor.execute("UPDATE Recipes SET cooking_time=%s, difficulty=%s WHERE id=%s", (new_value, difficulty, recipe_id))
    elif column == "ingredients":
        ingredients = [i.strip() for i in new_value.split(",")]
        difficulty = calculate_difficulty(
            cursor.execute("SELECT cooking_time FROM Recipes WHERE id=%s", (recipe_id,)).fetchone()[0],
            ingredients
        )
        cursor.execute("UPDATE Recipes SET ingredients=%s, difficulty=%s WHERE id=%s", (", ".join(ingredients), difficulty, recipe_id))
    else:
        cursor.execute(f"UPDATE Recipes SET {column}=%s WHERE id=%s", (new_value, recipe_id))

    conn.commit()
    print("Recipe updated successfully!")

# Part 6: Deleting a Recipe with delete_recipe()

def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for recipe in results:
        print(recipe)

    recipe_id = int(input("Enter recipe ID to delete: "))
    cursor.execute("DELETE FROM Recipes WHERE id=%s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

# Main Menu Loop
def main_menu(conn, cursor):
    while True:
        print("\nMain Menu")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Update Recipe")
        print("4. Delete Recipe")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            conn.commit()
            conn.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

#  Run the Program
if __name__ == "__main__":
    main_menu(conn, cursor)