from django.http import HttpResponse
from django.shortcuts import render

from recipe_app.models import Recipe, MealType, Ingredient, Measurement, RecipeName

from recipe_app.forms import IngredientForm, RecipeForm, RecipeNameForm, MeasurementForm


def addrecipe(request):
    if request.method == 'POST':
        recipe_name_form = RecipeNameForm(request.POST)
        measurement_form = MeasurementForm(request.POST)
        ingredient_form = IngredientForm(request.post)
        recipe_form = RecipeForm(request.POST)

        if recipe_name_form.is_valid() and measurement_form.is_valid() and ingredient_form.is_valid() and \
                recipe_form.is_valid():

            r = recipe_form.save()
            n = recipe_name_form.save(commit=False)
            m = measurement_form.save(commit=False)
            i = ingredient_form.save(commit=False)
            n.foreignkeytoRecipe = r
            r.save()
            m.foreignkeytoRecipe
    else:
        recipe_form = RecipeForm()
        measurement_form = MeasurementForm()
        ingredient_form = IngredientForm()
        recipe_name_form = RecipeForm()

    context = {'recipe_name_form': recipe_name_form, 'measurement_form': measurement_form, 'ingredient_form': ingredient_form,
               'recipe_form': recipe_form, }

    return render(request, 'addrecipe.html', context)