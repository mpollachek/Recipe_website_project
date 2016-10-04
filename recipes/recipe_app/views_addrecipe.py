from django.http import HttpResponse
from django.shortcuts import render

from recipe_app.models import Recipe, MealType, Ingredient

from recipe_app.forms import IngredientForm, RecipeForm


def addrecipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
    else:
        recipe_form = RecipeForm()

    context = {'recipe_form': recipe_form, }