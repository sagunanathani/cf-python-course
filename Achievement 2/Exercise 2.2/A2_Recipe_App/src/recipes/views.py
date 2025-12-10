from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'recipes/welcome.html')

def recipe_list(request):   # overview
    recipes = Recipe.objects.all()
    return render(request, 'recipes/overview.html', {'recipes': recipes})

def recipe_detail(request, pk): # detail
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

@login_required
def records(request): # protected
    recipes = Recipe.objects.all()
    return render(request, 'recipes/records.html', {'recipes': recipes})

