🧠 Learning Journal – Exercise 1.4: File Handling and Recipe Manager
📌 Overview
This exercise introduced me to Python file handling using both text and binary formats. I completed three tasks:

- Writing a list of numbers to a text file
- Storing and retrieving a recipe using binary files
- Building a two-part recipe manager that saves and searches recipes using binary serialization
  Each task helped reinforce key concepts like working with files, using dictionaries and lists, and structuring user-friendly terminal applications.

🧪 Practice Task 1 – Writing to Files

- Created a list of numbers from 50 to 100 using range().
- Used a with statement to open a file named number_list.txt in write mode.
- Saved the list to the file using writelines() with newline formatting.
- Verified the output and took a screenshot of the final step.
  📸 Screenshot

🧪 Practice Task 2 – Binary Files with Pickle

- Imported the pickle module.
- Created a dictionary for a tea recipe with name, ingredients, cooking time, and difficulty.
- Saved the dictionary to a binary file named recipe_binary.bin using pickle.dump().
- Loaded the data back using pickle.load() and printed it with readable formatting.
  📸 Screenshot

🧪 Recipe Manager – Full Project
Part 1: recipe_input.py

- Defined calc_difficulty() to classify recipes based on cooking time and number of ingredients.
- Created take_recipe() to collect recipe details from the user.
- Used a try-except-else-finally block to load or initialize recipe data from a binary file.
- Collected multiple recipes and updated two lists:
- recipes_list for full recipe dictionaries
- all_ingredients for unique ingredients
- Saved the updated data back to the binary file using pickle.dump().
  📸 Screenshots:

  Part 2: recipe_search.py

- Loaded the binary file using pickle.load().
- Displayed all available ingredients with index numbers.
- Allowed the user to select an ingredient by number.
- Printed full recipe details (name, cooking time, ingredients, difficulty) for each match using display_recipe().
  📸 Screenshot:

✅ What I Learned

- How to write and read text files using with open().
- How to use the pickle module to serialize and deserialize Python objects.
- How to structure data using dictionaries and lists for real-world use cases.
- How to use try-except-else-finally blocks to handle file errors gracefully.
- How to write modular code using functions for better readability and reuse.
- How to format output clearly for users in the terminal.

💬 Reflection
This exercise helped me understand how to persist data between sessions using both text and binary files. I practiced writing user-friendly terminal applications, handling edge cases like missing files or invalid input, and organizing code into reusable functions. I feel more confident now in building small utilities that store and retrieve structured data, and I’m excited to apply these skills to future projects.
