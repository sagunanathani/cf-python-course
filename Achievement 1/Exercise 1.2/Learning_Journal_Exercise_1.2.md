Learning Journal – Exercise 1.2 (Practice Tasks 1–5 + Recipe App Task)
📘 Overview

In Exercise 1.2, I practiced Python fundamentals across different core data structures: files, tuples, lists, strings, dictionaries, and finally combining everything in the Recipe App task. Each task strengthened my understanding of how to store, manipulate, and structure data in Python.

📝 Practice Task 1 – Files
I practiced reading data from a text file using open(), readlines(), and stripping newline characters. I learned how important it is to check the current working directory using os.getcwd() and update it with os.chdir() before reading files. This task helped me understand file handling and how Python interacts with the file system.

📝 Practice Task 2 – Tuples
I created a tuple containing world population data for several years. I practiced slicing the tuple to extract every third value and used max() to find the highest value in the sliced data. This reinforced the immutability of tuples and how slicing works on sequential data.

📝 Practice Task 3 – Lists
I created a list of Ford 2020 vehicle models and added a missing item ("Mustang") using append(). Then I sorted the list alphabetically using sort(). This task helped me understand the flexibility of lists and how easily they can be modified or reordered.

📝 Practice Task 4 – Strings
I explored string slicing using a predefined variable str3. I manually worked out the results for:
str3[3:]
str3[-3:]
str3[2:9:3]
str3[::-2]
str3[2:8]

This exercise strengthened my understanding of string indexing, slicing, stepping, and reverse slicing.

📝 Practice Task 5 – Dictionaries
I created two lists: month names and month numbers. Then I used zip() to combine them into a dictionary (months_dict). After that, I cleared the original lists using .clear() and extracted dictionary keys back into a new list. Sorting the extracted list helped me understand dictionary-to-list conversions and data reorganization.

📝 Practice Task 6 – Recipe App (Mini Project)
Choice of Data Structure
For each recipe, I used a dictionary because it allows storing multiple attributes (name, cooking time, ingredients) with meaningful keys. It is flexible, easy to extend, and readable.
For the outer collection all_recipes, I used a list, as it allows sequential storage of multiple recipes with easy iteration and modification.

Steps Completed
✔ Created recipe_1 for "Tea"
name: "Tea"
cooking_time: 5
ingredients: ["Tea leaves", "Sugar", "Water"]

✔ Created all_recipes and added recipe_1
✔ Created 4 more recipes (recipe_2 to recipe_5)
✔ Added all recipes to the outer list
✔ Printed ingredients for each recipe

This task helped me combine multiple Python concepts together: dictionaries, lists, nested structures, iteration, and data organization.

📚 Key Learnings
How to choose the right data structure depending on the requirement
Tuples for fixed data
Lists for ordered and editable data
Dictionaries for structured, attribute-based information
File handling with directories and reading line-by-line
Practical slicing with strings and tuples
Using zip() to merge lists efficiently
Structuring nested data for real-world applications (Recipe App)

🎯 Reflection
This exercise improved my confidence in using Python’s core data structures together. The Recipe App task especially helped me think about how real applications structure and store data. I also improved my troubleshooting skills when dealing with file paths and the IPython environment.
