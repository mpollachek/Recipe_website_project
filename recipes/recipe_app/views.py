from django.http import HttpResponse
from django.shortcuts import render

from recipe_app.models import Recipe, MealType, Ingredient, RecipeRating

from recipe_app.forms import RatingForm, IngredientForm, RecipeForm, SearchRecipeForm


def home(request):

    if request.method == 'POST':
        form = SearchRecipeForm(request.POST)
        if form.is_valid():

            all_recipes = Recipe.objects.all()


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