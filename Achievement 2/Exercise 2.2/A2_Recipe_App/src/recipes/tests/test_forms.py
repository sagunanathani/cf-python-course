from django.test import TestCase
from recipes.forms import RecipeSearchForm

class RecipeFormTest(TestCase):
    def test_form_valid_with_query(self):
        form = RecipeSearchForm(data={"query": "pasta", "difficulty": "", "show_all": False})
        self.assertTrue(form.is_valid())

    def test_form_valid_show_all(self):
        form = RecipeSearchForm(data={"show_all": True})
        self.assertTrue(form.is_valid())