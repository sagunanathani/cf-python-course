from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    # path('', views.welcome, name='welcome'),
    path('overview/', views.recipe_list, name='overview'),
    path('detail/<int:pk>/', views.recipe_detail, name='detail'),
]