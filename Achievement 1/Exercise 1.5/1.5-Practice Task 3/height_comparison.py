class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return str(self.feet) + " feet, " + str(self.inches) + " inches"

    # Less than (<)
    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    # Less than or equal to (<=)
    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    # Equal to (==)
    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

    # Greater than (>)
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    # Greater than or equal to (>=)
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    # Not equal to (!=)
    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


# --- Script Execution / Test Cases ---
print("Height(4, 6) > Height(4, 5):", Height(4, 6) > Height(4, 5))
print("Height(4, 5) >= Height(4, 5):", Height(4, 5) >= Height(4, 5))
print("Height(5, 9) != Height(5, 10):", Height(5, 9) != Height(5, 10))