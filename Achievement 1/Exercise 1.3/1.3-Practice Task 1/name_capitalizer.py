# Simple calculator for addition and subtraction

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+ or -): ")

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
else:
    print("Unknown operator. Please use + or -.")

pets = ['Dog', 'Iguana', 'Cat', 'Snake', 'Turtle']
for i in range(0, 3):
    print(pets[i])