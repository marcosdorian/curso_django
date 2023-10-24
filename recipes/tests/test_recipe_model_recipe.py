from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        # creating recipes with no defaults
        # look at the model Recipe
        recipe = Recipe(
            category=self.make_category(name='Test Category'),
            author=self.make_author(username='testuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-title-1',
            preparation_time='10',
            preparation_time_unit='Minutes',
            servings='5',
            servings_time_unit='Portions',
            preparation_steps='Recipe Preparation Steps',
            cover='recipes/covers/2023/10/16/download.jpeg',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    # this parameterized is used so Python can read the subgroups of tests
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_time_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        # testing all the fields at once
        # to attribute dynamic values, use setattr
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            # full_clean validates the rules of chars manually
            self.recipe.full_clean()
    # this test tries to create title, description, prepap. and servings
    # longer than their max_length, the test will pass because
    # it giver the error based on the declination to create these fields

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        # if you check on the model, this field is set to be False as default
        # the test passes if it is false when created
        # if it is True, the test fails
        recipe = self.make_recipe_no_defaults()
        # using the recipe created above
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not false'
        )

    def test_recipe_is_published_is_false_by_default(self):
        # if you check on the model, this field is set to be False as default
        # the test passes if it is false when created
        # if it is True, the test fails
        recipe = self.make_recipe_no_defaults()
        # using the recipe created above
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not false'
        )

    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), 'Testing Representation',
            msg=f'Recipe string representation must be '
                f'"{needed}" but it received "{str(self.recipe)}"'
        )
