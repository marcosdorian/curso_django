from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    # This method (setUp) runs before a test starts
    # So it creates a new recipe when necessary
    def setUp(self) -> None:
        # creating data for the tests
        return super().setUp()

    def make_category(self, name='Snacks'):
        return Category.objects.create(name=name)

    def make_author(
            self,
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
            self,
            category_data=None,
            author_data=None,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-title',
            preparation_time='10',
            preparation_time_unit='Minutes',
            servings='5',
            servings_time_unit='Portions',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
            cover='recipes/covers/2023/10/16/download.jpeg',
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            # this ** unpacks the dictionary
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_time_unit=servings_time_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
        )
