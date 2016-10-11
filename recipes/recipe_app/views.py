from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import generic

from recipe_app.models import Recipe, MealType, Ingredient, RecipeRating

from recipe_app.forms import RatingForm, RecipeForm, SearchRecipeForm


def home(request):

    queryset_list = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = Recipe.objects.all().filter(Q(title__icontains=query) | Q(ingredients__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 25)




    context = {
        "queryset_results": queryset_list
    }
    return render(request, "home.html", context)


"""
    if request.method == 'POST':
        search_recipe_form = SearchRecipeForm(request.POST)
        if search_recipe_form.is_valid():

            #all_recipes = Recipe.objects.all()
            clean_title = search_recipe_form.cleaned_data['title']
            clean_ingredients = search_recipe_form.cleaned_data['ingredients']
            results = Recipe.objects.filter(Q(title__icontains=clean_title) | Q(ingredients__icontains=clean_ingredients))

            """
"""
            results = Recipe.objects.get(
                #Q(title__icontains='search_recipe_form.cleaned_data.iteritems()) |
                Q(ingredients__icontains='search_recipe_form.cleaned_data.iteritems())
            )
"""
"""

        else:
            search_recipe_form = SearchRecipeForm()
            clean_title = search_recipe_form.cleaned_data['title']
            clean_ingredients = search_recipe_form.cleaned_data['ingredients']

    else:
        search_recipe_form = SearchRecipeForm()
        clean_title = search_recipe_form
        clean_ingredients = search_recipe_form

    context = {'search_recipe_form': search_recipe_form, 'clean_title': clean_title,
               'clean_ingredients': clean_ingredients,}

    return results

    #return render(request, 'recipesearch.html', context)

"""
#Lookup AJAX for autocomplete feature


def recipesearch(request):
    pass


def favorites(request):
    pass


def toprated(request):
    pass


def myrecipes(request):
    pass


def contact(request):
    pass


def about(request):
    pass