from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeModelTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Test Pasta",
            author_name="Chef Sage",
            ingredients="Pasta\nTomato\nSalt",
            instructions="Boil pasta.\nMake sauce.\nCombine.",
            prep_time=10,
            cook_time=20,
            serves=2
        )

    def test_total_time(self):
        self.assertEqual(self.recipe.total_time(), 30)

    def test_difficulty(self):
        self.assertEqual(self.recipe.difficulty(), "Easy")

    def test_get_absolute_url(self):
        expected = reverse('recipes:detail', kwargs={'pk': self.recipe.pk})
        self.assertEqual(self.recipe.get_absolute_url(), expected)