from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.template.loader import get_template
from django.views import generic


from recipe_app.forms import RecipeForm, SearchRecipeForm, ContactForm, IngredientFormSet
from recipe_app.models import Recipe, MealType, Ingredient




def home(request):

    queryset_list = Recipe.objects.all() #.order_by(RecipeRating)

    query = request.GET.get("q")

    #if request.method == 'POST':
    if query:
        queryset_list = Recipe.objects.filter(Q(recipe_name__icontains=query) |
                                              Q(ingredient__ingredient_name__icontains=query)).distinct()\
                                               .order_by('-ratings__average')

        context = {
            "queryset_results": queryset_list,
            #"page_request_var": page_request_var
        }
        return render(request, "home.html", context)

    else:

        context = {
            "queryset_results": queryset_list
        }
        return render(request, "home.html", context)

"""
        paginator = Paginator(queryset_list, 25)
        page_request_var = "page"
        page = request.Get.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
"""



"""
    if request.method == 'POST':
        search_recipe_form = SearchRecipeForm(request.POST)
        if search_recipe_form.is_valid():

            #all_recipes = Recipe.objects.all()
            clean_name = search_recipe_form.cleaned_data['name']
            clean_ingredients = search_recipe_form.cleaned_data['ingredients']
            results = Recipe.objects.filter(Q(name__icontains=clean_name) | Q(ingredients__icontains=clean_ingredients))

            """
"""
            results = Recipe.objects.get(
                #Q(name__icontains='search_recipe_form.cleaned_data.iteritems()) |
                Q(ingredients__icontains='search_recipe_form.cleaned_data.iteritems())
            )
"""
"""

        else:
            search_recipe_form = SearchRecipeForm()
            clean_name = search_recipe_form.cleaned_data['title']
            clean_ingredients = search_recipe_form.cleaned_data['ingredients']

    else:
        search_recipe_form = SearchRecipeForm()
        clean_name = search_recipe_form
        clean_ingredients = search_recipe_form

    context = {'search_recipe_form': search_recipe_form, 'clean_name': clean_name,
               'clean_ingredients': clean_ingredients,}

    return results

    #return render(request, 'recipesearch.html', context)

"""
#Lookup AJAX for autocomplete feature


def recipe_detail(request, id=None):
    instance = get_object_or_404(Recipe, id=id)

    context = {
        "rec": instance
    }
    return render(request, "recipe_detail.html", context)


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        ingredient_form = IngredientFormSet(request.POST, instance=recipe)

        if recipe_form.is_valid():
            created_recipe = recipe_form.save(commit=False,)
            created_recipe.author = request.user
            ingredient_form = IngredientFormSet(request.POST, instance=created_recipe)

            if ingredient_form.is_valid():
                created_recipe.save()
                ingredient_form.save()
                return HttpResponseRedirect(created_recipe.get_absolute_url())

    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientFormSet(instance=recipe)

    context = {
        'ingredient_form': ingredient_form,
        'recipe_form': recipe_form,
    }
    return render(request, "addrecipe.html", context)


def recipe_delete(request):
    instance = get_object_or_404(Recipe, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("recipes:home")


def favorites(request):
    pass


def toprated(request):
    queryset_list = Recipe.objects.all().order_by('-ratings__average')


    context = {
        "queryset_results": queryset_list,
        }
    return render(request, "toprated.html", context)


def myrecipes(request):
    pass


def contact(request):
    contact_form = ContactForm

    if request.method == 'POST':
        form = contact_form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            email = EmailMessage("New contact form submission",
                                 content,
                                 "Baller Recipes" + '',
                                 ['mpollachek81@gmail.com']
                                 )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html', {'contact_form': contact_form})


def about(request):
    return render(request, 'about.html')