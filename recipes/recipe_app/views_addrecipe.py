from django.forms.models import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from recipe_app.forms import RecipeForm, IngredientFormSet
from recipe_app.models import Recipe, MealType, Ingredient




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
    recipe = Recipe()
    #recipe = Recipe.objects.get(Recipe, pk=recipe_pk)

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
                created_recipe = recipe_form.save(commit=False)
                created_recipe.author = request.user
                ingredient_form = IngredientFormSet(request.POST, instance=created_recipe)

                if ingredient_form.is_valid():
                    created_recipe.save()
                    ingredient_form.save()
                    return HttpResponseRedirect(created_recipe.get_absolute_url())

                #ings = ingredient_form.save(commit=False)
                #for ing in ings:
                    #ingredient.recipe = recipe
                    #ing.save()

    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientFormSet(instance=recipe)

    context = {'ingredient_form': ingredient_form,
               'recipe_form': recipe_form, }

    return render(request, 'addrecipe.html', context)
