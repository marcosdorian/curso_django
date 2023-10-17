from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RecipeUrlsTest(TestCase):
    # testing if the url "home" is designed to be "/"
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
    
    # testing if the url "category" is designed to be "/" and the id given
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    # testing if the url "recipe" is designed to be "/" and the id given
    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')