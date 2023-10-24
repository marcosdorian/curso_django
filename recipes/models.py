from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)

    # calling the model as a string
    # it will show as the name of the category
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_time_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    # creating the relation between the tables (Category and Recipe)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    # creating the relation between the tables (User and Recipe)
    # The table "User" comes from Django and it's imported
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True, default=None)

    # calling the model as a string
    # it will show as the name of the recipe
    def __str__(self):
        return self.title
