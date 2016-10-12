from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from recipe_app.models import Recipe, MealType, Ingredient

from recipe_app.forms import RecipeForm, IngredientFormSet
from django.forms.models import formset_factory




"""
class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'addrecipe.html'
    form_class = RecipeForm

    def post(self):
        ingredient_form = IngredientFormSet()
        measurement_form = MeasurementFormSet()
        return render(request, 'addrecipe.html')
"""

"""
def addrecipe(request):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.post)
        recipe_form = RecipeForm(request.POST)

        if ingredient_form.is_valid() and recipe_form.is_valid():

    else:
        ingredient_form = IngredientForm()
        recipe_form = RecipeForm()

    context = {'ingredient_form': ingredient_form,
               'recipe_form': recipe_form, }

    return render(request, 'addrecipe.html', context)
"""