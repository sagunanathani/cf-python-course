from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import RecipeForm
from .models import Recipe
from django.urls import reverse
from .forms import RecipeSearchForm
import pandas as pd
import io
import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def home(request):
    return render(request, 'recipes/welcome.html') # root → welcome page

def recipe_list(request):   # overview
    recipes = Recipe.objects.all()
    return render(request, 'recipes/overview.html', {'recipes': recipes})

def recipe_detail(request, pk): # detail
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def about_me(request):
    return render(request, 'recipes/about_me.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def records(request):  # protected
    records = Recipe.objects.all()
    return render(request, 'recipes/records.html', {'records': records})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # link recipe to logged-in user
            recipe.save()
            return redirect('recipes:overview')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def search(request):
    form = RecipeSearchForm(request.GET or None)
    qs = Recipe.objects.none()
    results_df = None
    charts = {}

    if form.is_valid():
        query = form.cleaned_data.get("query", "").strip()
        show_all = form.cleaned_data.get("show_all")

        qs = Recipe.objects.all() if show_all else Recipe.objects.all()

        # Wildcard/partial search on multiple fields
        if query and not show_all:
            qs = qs.filter(
                title__icontains=query
            ) | qs.filter(
                description__icontains=query
            ) | qs.filter(
                ingredients__icontains=query
            )

        # Convert QuerySet → DataFrame (only valid fields!)
        results_df = pd.DataFrame.from_records(
            qs.values("title", "prep_time", "cook_time", "serves")
        )

        # ✅ Generate charts only if we have results
        if not results_df.empty:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            import io, base64

            # Bar chart: Servings per recipe
            fig, ax = plt.subplots(figsize=(6,4))
            results_df.plot.bar(x="title", y="serves", color="#ff7043", ax=ax)
            
            ax.set_xlabel("Recipe Name"); ax.set_ylabel("Serving Time(min)")
            buf = io.BytesIO(); plt.tight_layout(); plt.savefig(buf, format="png"); buf.seek(0)
            charts["bar"] = base64.b64encode(buf.getvalue()).decode("utf-8"); plt.close(fig)

            # Pie chart: Cook time distribution
            fig, ax = plt.subplots(figsize=(6,4))
            results_df.set_index("title")["cook_time"].plot.pie(autopct="%1.0f%%", ax=ax)
            ax.set_ylabel(""); ax.set_title("Cook Time Distribution")
            buf = io.BytesIO(); plt.tight_layout(); plt.savefig(buf, format="png"); buf.seek(0)
            charts["pie"] = base64.b64encode(buf.getvalue()).decode("utf-8"); plt.close(fig)

            # Line chart: Prep time trend
            df_sorted = results_df.sort_values("title")
            fig, ax = plt.subplots(figsize=(7,4))
            ax.plot(df_sorted["title"], df_sorted["prep_time"], marker="o", color="#ff7043")
            ax.set_title("Prep Time by Recipe")
            ax.set_xlabel("Recipe Name"); ax.set_ylabel("Prep Time(Min)")
            plt.xticks(rotation=45, ha="right")
            buf = io.BytesIO(); plt.tight_layout(); plt.savefig(buf, format="png"); buf.seek(0)
            charts["line"] = base64.b64encode(buf.getvalue()).decode("utf-8"); plt.close(fig)

    context = {
        "form": form,
        "results": qs,
        "results_df": results_df,
        "charts": charts,
        "detail_url_name": "recipes:detail",
    }
    return render(request, "recipes/search.html", context)

