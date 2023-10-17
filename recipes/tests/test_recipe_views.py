from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    # testing if the funcion of "home" is working correctly
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        # checking if the function inside "view" is the same as "views.home"
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        # checking if the function inside "view" is the same as in category
        self.assertIs(view.func, views.category)

    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        # checking if the function inside "view" is the same as "views.recipe"
        self.assertIs(view.func, views.recipe)
    
    def test_recipe_home_view_returns_status_code_200_ok(self):
        # checking if this page returns the response 200
        # this client is given by django.test
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_view_loads_correct_template(self):
        # checking if the templase is used correctly
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')