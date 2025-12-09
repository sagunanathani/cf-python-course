from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=150, default="Untitled Recipe")
    author_name = models.CharField(max_length=120, default="Unknown")
    description = models.TextField(blank=True)
    ingredients = models.TextField(default="No ingredients listed")
    instructions = models.TextField(default="No instructions yet")
    prep_time = models.IntegerField(help_text="Minutes", default=0)
    cook_time = models.IntegerField(help_text="Minutes", default=0) 
    serves = models.IntegerField(default=1)
    image = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return self.title

    def total_time(self):
        return (self.prep_time or 0) + (self.cook_time or 0)
 
    def difficulty(self):
        # Example logic (adjust per Achievement 1 rules)
        # Easy: <= 30 min and <= 6 ingredients
        # Medium: <= 60 min or <= 10 ingredients
        # Hard: > 60 min or > 10 ingredients
        ing_count = len([i for i in self.ingredients.splitlines() if i.strip()])
        t = self.total_time()
        if t <= 30 and ing_count <= 6:
            return "Easy"
        if t <= 60 or ing_count <= 10:
            return "Medium"
        return "Hard"

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})