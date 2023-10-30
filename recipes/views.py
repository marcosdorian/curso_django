from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
from django.db.models import Q


# Create your views here.
def home(request):
    recipes = Recipe.objects.all().filter(
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'

    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    # strip() to avoid empty spaces
    # so users cannot search without typing a word
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        # I used __contains so SQL find what is inbetween the name
        # If I don't use this, I will have to search exactly the same name
        # Search for "bolo", but the name is "bolo de banana", it will find
        # i before contains is used to ignore capslock or lower
        # this Q is used to say to SQL that it's OR
        # you search by title OR description
        # Q is an imported library
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        # it only shows the published recipes
        is_published=True,
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes,
    })
