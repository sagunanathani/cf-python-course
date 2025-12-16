from django.urls import path
from . import views
from .views import home, recipe_list, recipe_detail, records

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('overview/', recipe_list, name='overview'),
    path('detail/<int:pk>/', recipe_detail, name='detail'),   # detail for overview list
    path('records/', views.records, name='records'),                # records overview
    path('records/<int:pk>/', views.recipe_detail, name='record_detail'),  # detail for records
    path('search/', views.search, name='search'),
    path('add/', views.add_recipe, name='add'), # add recipes
]