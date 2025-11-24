# Exercise 1.5 – Practice Tasks

This folder contains my solutions for **Exercise 1.5 Practice Tasks** from the Code First Python course.  
Each task demonstrates object-oriented programming concepts in Python, including class definitions, methods, operator overloading, and comparison operators.

---

## 📂 Contents

- `practice_task1.py` → Shopping List class
- `practice_task2.py` → Height class with addition and subtraction
- `practice_task3.py` → Height class with comparison operators
- Screenshots of execution (named consistently per task)
- `Learning_Journal.md` → Reflections and notes

---

## 📝 Practice Task 1 – Shopping List

### Overview

I created a `ShoppingList` class to manage items in a shopping list.  
It supports adding, removing, and viewing items, while preventing duplicates.

### Key Features

- `add_item()` → Adds items if not already present
- `remove_item()` → Removes items if they exist
- `view_list()` → Displays the list with numbering

### Example Execution

- Added items: dog food, frisbee, bowl, collars, flea collars
- Removed: flea collars
- Attempted duplicate: frisbee
- Final list displayed with numbering

📸 Screenshot: `Task1_ShoppingList.png`

---

## 📝 Practice Task 2 – Height Class (Operator Overloading)

### Overview

I created a `Height` class to represent heights in feet and inches.  
I implemented operator overloading for **addition** and **subtraction**.

### Key Features

- `__add__()` → Adds two heights
- `__sub__()` → Subtracts one height from another
- `__str__()` → Returns a readable string format

### Example Execution

- h1 = 5 feet 10 inches
- h2 = 3 feet 9 inches
- Subtraction: `h1 - h2 = 2 feet, 1 inches`

📸 Screenshot: `Task2_Height_Subtraction.png`

---

## 📝 Practice Task 3 – Height Class (Comparison Operators)

### Overview

I extended the `Height` class to support **comparison operators**.  
This allows comparing heights using `<, <=, ==, >, >=, !=`.

### Key Features

- `__lt__()` → Less than
- `__le__()` → Less than or equal
- `__eq__()` → Equal to
- `__gt__()` → Greater than
- `__ge__()` → Greater than or equal
- `__ne__()` → Not equal

### Example Execution

- `Height(4, 6) > Height(4, 5)` → True
- `Height(4, 5) >= Height(4, 5)` → True
- `Height(5, 9) != Height(5, 10)` → True

📸 Screenshot: `Task3_Height_Comparison.png`

---

# 📖 Learning Journal – Exercise 1.5

### What I Did

- Built three Python classes (`ShoppingList`, `Height` with arithmetic, `Height` with comparisons).
- Practiced **object-oriented programming** concepts:
  - Encapsulation (data + methods together)
  - Operator overloading (`__add__`, `__sub__`)
  - Comparison operators (`__lt__`, `__eq__`, etc.)
- Tested each class with sample data and printed results.

### What I Learned

- How classes make code more modular and reusable compared to procedural approaches.
- How operator overloading allows intuitive use of `+`, `-`, and comparison operators on custom objects.
- How to design methods that handle both data conversion (feet/inches → total inches) and output formatting.
- The importance of clean string representations (`__str__`) for debugging and user-friendly output.

### Reflection

This exercise helped me strengthen my understanding of OOP in Python.  
I now feel more confident in:

- Designing classes with clear responsibilities
- Using operator overloading to make custom objects behave like built-in types
- Writing comparison methods to extend functionality naturally

These skills will be useful in larger projects, such as recipe management or portfolio applications, where modular design and reusability are critical.

---
