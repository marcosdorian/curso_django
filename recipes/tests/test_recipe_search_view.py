from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):
    # testing if the page of search is working properly
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        # since I said that the page cannot load without a search word
        # I must add a word to test the search engine
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        response = self.client.get(reverse('recipes:search') + '?q=<Test>')
        self.assertIn(
            # it must be written like this because it's not escaped
            # checking a suspect search term
            # to escape value you must use for example:
            # seach_term/safe
            'Search for &quot;&lt;Test&gt;&quot;',
            response.content.decode('utf-8')
        )
