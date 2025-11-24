# Define a class to manage a shopping list
class ShoppingList:
    def __init__(self, list_name):
        # Initialize the shopping list with a name and an empty list of items
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        # Add an item only if it is not already in the list
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"✅ '{item}' added to the list.")
        else:
            # Warn if the item is already present
            print(f"⚠️ '{item}' is already in the list.")

    def remove_item(self, item):
        # Remove an item if it exists in the list
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"❌ '{item}' removed from the list.")
        else:
            # Warn if the item is not found
            print(f"⚠️ '{item}' not found in the list.")

    def view_list(self):
        # Display the shopping list name and its contents
        print(f"\n🛒 {self.list_name}")
        if self.shopping_list:
            # Print each item with its index number
            for index, item in enumerate(self.shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            # Inform if the list is empty
            print("The shopping list is currently empty.")


# --- Script Execution ---

# Create the shopping list object with a name
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items to the shopping list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item from the list
pet_store_list.remove_item("flea collars")

# Try adding a duplicate item (should show a warning)
pet_store_list.add_item("frisbee")

# View the final shopping list
pet_store_list.view_list()