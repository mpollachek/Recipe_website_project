from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from recipe_app.models import Recipe, MealType, Ingredient, RecipeRating

from recipe_app.forms import RatingForm, IngredientForm, RecipeForm, SearchRecipeForm


def home(request):

    if request.method == 'POST':
        form = SearchRecipeForm(request.POST)
        if form.is_valid():

            #all_recipes = Recipe.objects.all()
            Recipe.object.get(
                Q(title__icontains='form.cleaned_data.iteritems()) |
                Q(ingredients__icontains='form.cleaned_data.iteritems())
            )

    return render(request, 'home.html', )


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