Exercise 1.2 – Code Practice 1: Types & Calculations
📘 Overview

This exercise focuses on using Python variable assignment, data types, explicit type conversion, and performing a compound interest calculation using values stored in a text file.

📝 Steps Completed

1. Created codepractice1.txt
   The file contains three values on separate lines:

1000
0.145
3

These represent:
Principal amount
Interest rate
Time period (years)

2. Navigated to the Exercise directory in IPython
   import os
   os.chdir(r"C:\Users\Saguna Nathani\Desktop\CF_Projects\cf-python-course\Exercise 1.2")
   os.listdir()

3. Loaded values from the text file
   f = open('codepractice1.txt', 'r')
   lines = f.readlines()
   [principal, rate, time_period] = [x.strip('\n') for x in lines]
   f.close()

4. Converted all values to float
   principal = float(principal)
   rate = float(rate)
   time_period = float(time_period)

5. Calculated the Compounded Principal

Using the formula:
Compounded Principal = Principal × (1 + Rate) ^ Time_Period

compounded_principal = principal \* (1 + rate) \*\* time_period
compounded_principal

6. Uploaded Deliverables to GitHub

Inside Exercise 1.2 → 1.2-Practice Task 1, uploaded:

✔️ Screenshots for each step
✔️ codepractice1.txt
✔️ This README.md

📚 What I Learned
How to read values from a text file in Python
How data types affect calculations
How to convert strings to floats
Using exponentiation (\*\*) to calculate compound interest
Navigating directories from inside IPython
Properly organizing exercises in a GitHub repository
