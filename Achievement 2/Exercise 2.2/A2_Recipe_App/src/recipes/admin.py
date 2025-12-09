from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'serves', 'prep_time', 'cook_time')
    search_fields = ('title', 'author_name')