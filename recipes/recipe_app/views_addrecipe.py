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
        recipe_form = RecipeForm
        return render(request, 'addrecipe.html')

"""


def addrecipe(request, recipe_pk):
    recipe = Recipe.objects.get(Recipe, pk=recipe_pk)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientFormSet(request.POST, instance=recipe)

        #if 'add_ingredient' in request.POST:
            #pass
            #cp = request.POST.copy()
            #cp['ing-TOTAL_FORMS'] = int(cp['ing-TOTAL_FORMS']) + 1
            #ings = ingredient_form(cp, prefix='ing')

        if 'submit' in request.POST:
            if recipe_form.is_valid():
                recipe_form.save()
            if ingredient_form.is_valid():
                ingredient_form.save()
                #ings = ingredient_form.save(commit=False)
                #for ing in ings:
                    #ingredient.recipe = recipe
                    #ing.save()

    else:
        recipe_form = RecipeForm()
        ingredient_form = IngredientFormSet(instance=recipe)

    context = {'ingredient_form': ingredient_form,
               'recipe_form': recipe_form, }

    return render(request, 'addrecipe.html', context)
