# Step 1: Create the list of test scores
test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]

# Step 2: Sort the list in descending order
test_scores.sort(reverse=True)

# sorted list
print(test_scores)

# Step 3: Print the top 3 scores using a for loop
print("Top 3 scores:")
for i in range(3):
    print(test_scores[i])

