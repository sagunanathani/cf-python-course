from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe

class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="saguna", password="pass123")
        Recipe.objects.create(title="Pasta", difficulty="Easy", prep_time=10, cook_time=15, description="Yum", ingredients="Wheat")
        Recipe.objects.create(title="Spicy Curry", difficulty="Hard", prep_time=20, cook_time=40, description="Hot", ingredients="Spices")

    def test_search_requires_login(self):
        url = reverse("recipes:search")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)  # redirect to login

    def test_search_results(self):
        self.client.login(username="saguna", password="pass123")
        url = reverse("recipes:search")
        resp = self.client.get(url, {"query": "pasta"})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Pasta")

    def test_charts_requires_login(self):
        url = reverse("recipes:charts")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_charts_render(self):
        self.client.login(username="saguna", password="pass123")
        url = reverse("recipes:charts")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Data visualization")