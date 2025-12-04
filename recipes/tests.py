from django.test import TestCase
from .models import Recipe

# Create tests here.
class RecipeModelTest(TestCase):
    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            name="Pasta",
            description="Creamy Alfredo pasta",
            cooking_time=20,
            difficulty="Easy"
        )
        self.assertEqual(recipe.name, "Pasta")