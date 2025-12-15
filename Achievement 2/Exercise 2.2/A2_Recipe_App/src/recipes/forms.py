from django import forms

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