from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context
from django.template.loader import get_template
from django.views import generic


from recipe_app.forms import RecipeForm, SearchRecipeForm, ContactForm, IngredientFormSet, FavoriteForm, \
    MealTypeForm
from recipe_app.models import Recipe, MealType, Ingredient, Favorite




def home(request):

    context = {}
    mealtypes = []
    query = request.GET.get("q")

    #if request.method == 'POST':
    if query:
        for mt in request.GET.getlist('mealtype'):
            mealtypes.append(mt)
            #print mealtypes
        queryset_list = Recipe.objects.filter(meal_type__name__in=mealtypes)\
            .filter(Q(recipe_name__icontains=query) |
                    Q(ingredient__ingredient_name__icontains=query)).distinct()\
            .order_by('-ratings__average')

        count = queryset_list.count()
        context = {
            "queryset_results": queryset_list,
            "count": count,
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

#Lookup AJAX for autocomplete feature


def recipe_detail(request, id=None):
    instance = get_object_or_404(Recipe, id=id)
    #favorite_form = FavoriteForm(request.POST)
    #if request.method == 'POST':
        #if 'favorite' in request.POST:
            #if favorite_form.is_valid():
                #form = favorite_form.save(commit=False)
                #form.fav_user = request.user
                #form.fav_recipe = instance
                #form.save()

    #fav = request.POST("favorite")
    #if fav:
        #f = Favorite(fav_recipe=instance, fav_user=request.user)
        #f.save()

    context = {
        "rec": instance,
        #"favorite_form": favorite_form,
            }
    return render(request, "recipe_detail.html", context)


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        ingredient_form = IngredientFormSet(request.POST, instance=recipe)

        if recipe_form.is_valid():
            created_recipe = recipe_form.save(commit=False)
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

    favorites_list = Favorite.objects.filter(fav_user=request.user).order_by('-fav_recipe')
    count = favorites_list.count()

    context = {
        "favorites_list": favorites_list,
        "count": count,
    }

    return render(request, "favorites.html", context)


def toprated(request):
    queryset_list = Recipe.objects.all().order_by('-ratings__average')


    context = {
        "queryset_results": queryset_list,
        }
    return render(request, "toprated.html", context)


def myrecipes(request):
    myrecipes_list = Recipe.objects.filter(author=request.user).order_by('recipe_name')

    count = myrecipes_list.count()
    context = {
        "myrecipes_list": myrecipes_list,
        "count": count,
    }

    return render(request, "myrecipes.html", context)


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