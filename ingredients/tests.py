from django.test import TestCase
from .models import Ingredient

# Create tests here.
class IngredientModelTest(TestCase):
    def test_create_ingredient(self):
        ingredient = Ingredient.objects.create(
            name="Tomato"
        )
        # Check that the ingredient was created correctly
        self.assertEqual(ingredient.name, "Tomato")
        # Optional: check that the __str__ method returns the name
        self.assertEqual(str(ingredient), "Tomato")