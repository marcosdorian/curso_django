from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    # testing if the detail page is working properly
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

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It loads one recipe'
        # using the method from RecipeTestBase to create a new recipe
        self.make_recipe(title=needed_title)

        # testing if the new recipe is showing on this page
        response = self.client.get(reverse('recipes:recipe', kwargs={
            'id': 1
        }))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_doesnt_load_recipe_not_published(self):
        """Test recipe is_published False is not shown"""
        # using the method from RecipeTestBase to create a new recipe
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id})
        )

        # testing if the page will not load if there are no recipes published
        self.assertEqual(response.status_code, 404)
