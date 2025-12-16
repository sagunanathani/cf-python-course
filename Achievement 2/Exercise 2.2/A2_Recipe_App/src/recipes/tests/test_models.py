from django.test import TestCase
from recipes.models import Recipe

class RecipeModelTest(TestCase):
    def test_recipe_str(self):
        recipe = Recipe.objects.create(
            title="Soup",
            difficulty="Medium",
            prep_time=15,
            cook_time=30,
            description="Tasty tomato soup",
            ingredients="Tomatoes, salt, water"
        )
        # __str__ method should return the title
        self.assertEqual(str(recipe), "Soup")

    def test_recipe_fields(self):
        recipe = Recipe.objects.create(
            title="Cake",
            difficulty="Easy",
            prep_time=10,
            cook_time=20,
            description="Chocolate cake",
            ingredients="Flour, cocoa, sugar"
        )
        self.assertEqual(recipe.difficulty, "Easy")
        self.assertEqual(recipe.prep_time, 10)
        self.assertEqual(recipe.cook_time, 20)