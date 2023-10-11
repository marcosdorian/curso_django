from django.urls import path
from . import views

# recipes:home or recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]