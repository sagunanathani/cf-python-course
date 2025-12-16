from django import forms
from .models import Recipe

class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        label="Search recipes",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., Pasta, Vegan"})
    )
    show_all = forms.BooleanField(
        label="Show all recipes",
        required=False
    )

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']