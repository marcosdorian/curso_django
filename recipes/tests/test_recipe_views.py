from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    # testing if the funcion of "home" is working correctly
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        # checking if the function inside "view" is the same as "views.home"
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        # checking if this page returns the response 200
        # this client is given by django.test
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        # checking if the templase is used correctly
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_foung_if_no_recipes(self):
        # checking if there will be the page "not found" if
        # there are no recipes registered
        response = self.client.get(reverse('recipes:home'))
        # checking if there is the sentence 'No recipes found here'
        # in the content of the html in 'home'
        self.assertIn(
            'No Recipes Found Here',
            response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        # using the method from RecipeTestBase to create a new recipe
        # opening the dictionary to include a name
        self.make_recipe()
        # testing if the new recipe is showing on this page
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutes', content)

        # testing if only 1 recipe was created
        response_context_recipes = response.context['recipes']
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category',
                       kwargs={'category_id': 1000}))
        # checking if the function inside "view" is the same as in category
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        # checking if this page returns the response 404 in case of no recipes
        # this client is given by django.test
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_details_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        # checking if the function inside "view" is the same as "views.recipe"
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        # checking if this page returns the response 404 in case of no recipes
        # this client is given by django.test
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)
