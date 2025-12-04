from django.db import models

# Create models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    ingredients = models.ManyToManyField('ingredients.Ingredient')

    def __str__(self):
        return self.name