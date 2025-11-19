# First Example
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
first_name = first_name.capitalize()
last_name = last_name.capitalize()

print("My name is", first_name, last_name)

# Second Example
a = input("Enter a number: ")
b = input("Enter another number to be added to the first: ")
a = int(a)
b = int(b)
print("The sum of these numbers is", a + b)

# shorten code with Second Example
a = int(input("Enter a double digit number: "))
b = int(input("Enter another number to be added to the first like double digit number: "))
print("The sum of these numbers is " + str(a + b))

age = int(input("Enter your age: "))
print("Age between 96 and 98: " + str(96 < age < 98))

# The if-else Statement 
fruit = input("I have an apple, an orange and a banana! " \
    + "Which fruit would you like to have? : ")

if fruit == "apple":
    print("Here, have an apple!")

elif fruit == "orange":
    print("Here, have an orange!")

elif fruit == "banana":
    print("Here, have a banana!")

else:
    print("Oops, I don't think I have that.")

# Nested Statements
number_of_oranges = int(input("How many oranges do you have?: "))

if number_of_oranges > 0:
    print("You have some oranges.")

    if number_of_oranges > 50:
        print("But you've got way too many!")

else:
    print("You have no oranges.")

# for Loops
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[0])
print(planets[1])

# range(start, end, step)
for i in range(5, 11, 1):
    print(i)

# range() function
pets = ['Dog', 'Iguana', 'Cat', 'Snake', 'Turtle']
for i in range(0, 3):
    print(pets[i])

# while Loops
number = 5

while number < 11:
    print(number)
    number += 1   # We're incrementing 'number' by 1 here

# The break and continue Statements
num = int(input("Enter a number to be divided: "))
start = int(input("Enter a starting point for the divisor: "))
end = int(input("Enter an end point for the divisor: "))

for div in range(start, end):
    if div == 0:
        print("Division by zero, exiting.")
        break
    print(num / div)

# The enumerate() Function
fruits = ['Apples', 'Oranges', 'Bananas']

for element in fruits:
    print(element)

fruits = ['Apples', 'Oranges', 'Bananas']
count = 0

for element in fruits:
    print("Item " + str(count) + ": " + element)
    count += 1

# for <position>, <value> in enumerate(seq):
# You’ll use this syntax to run through the same example:

fruits = ['Apples', 'Oranges', 'Bananas']
for position, value in enumerate(fruits):
    print("Item " + str(position) + ": " + value)

fruits = ['Apples', 'Oranges', 'Bananas']
new_list = list(enumerate(fruits))
print(new_list)
# output : 
[(0, 'Apples'), (1, 'Oranges'), (2, 'Bananas')]

fruits = ['Apples', 'Oranges', 'Bananas']
new_list = list(enumerate(fruits, 100))
print(new_list)
# The result would then be:
[(100, 'Apples'), (101, 'Oranges'), (102, 'Bananas')]

# Function
# The function gets defined here, arguments
# value1 and value2 are set up to accept values.
def adder(value1, value2):
    result = value1 + value2
    print("The added result is " + str(result))

# The main code starts here. We'll take the user's inputs now.
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Calling adder() which prints the result
adder(a, b)

# Calling Functions with Keyword Arguments
# Here's a function that takes value1 and value2,
# divides value1 by value2 and then prints the result
def divider(value1, value2):
    print(value1 / value2)

# Taking the user's inputs:
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Calling divider() normally
divider(a, b)

# Calling divider() by passing keyword arguments
divider(value1 = a, value2 = b)