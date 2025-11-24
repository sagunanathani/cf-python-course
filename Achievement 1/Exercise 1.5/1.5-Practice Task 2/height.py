class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return str(self.feet) + " feet, " + str(self.inches) + " inches"

    def __add__(self, other):
        # Convert both heights to inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Add them
        total_height_inches = height_A_inches + height_B_inches

        # Convert back to feet and inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches % 12

        return Height(output_feet, output_inches)

    def __sub__(self, other):
        # Convert both heights to inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # Subtract them
        diff_inches = height_A_inches - height_B_inches

        # Convert back to feet and inches
        output_feet = diff_inches // 12
        output_inches = diff_inches % 12

        return Height(output_feet, output_inches)


# --- Script Execution ---
h1 = Height(5, 10)   # 5 feet 10 inches
h2 = Height(3, 9)    # 3 feet 9 inches

# Subtraction
result = h1 - h2
print(f"{h1} - {h2} = {result}")