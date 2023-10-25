from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    # testing Category View is working properly
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

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # using the method from RecipeTestBase to create a new recipe
        self.make_recipe(title=needed_title)

        # testing if the new recipe is showing on this page
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_doesnt_load_recipes_not_published(self):
        """Test recipe is_published False is not shown"""
        # using the method from RecipeTestBase to create a new recipe
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )

        # testing if the page will not load if there are no recipes published
        self.assertEqual(response.status_code, 404)
