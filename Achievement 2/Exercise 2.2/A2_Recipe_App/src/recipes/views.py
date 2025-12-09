from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    return render(request, 'recipes/welcome.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/overview.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'recipe': recipe})