from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.models import inlineformset_factory, formset_factory

from recipe_app.models import Ingredient, Recipe, RecipeRating, UserProfile, MealType, MEALTYPE_CHOICES, Measurement


class MealTypeForm(forms.Form):
    mt_field = forms.ModelMultipleChoiceField(choices=MEALTYPE_CHOICES, widget=forms.CheckboxSelectMultiple)  #queryset=MealType.objects.all instead of choices

    Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe)

    def __unicode__(self):
        return "{}".format(self.name)


class Measurement(models.Model):
    amount = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    ingredient = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return "{} {}".format(self.amount, self.unit)


class SearchRecipeForm(forms.TextInput):
    class Meta:
        model = Recipe
        fields = ['title', 'meal_type', 'ingredients',]


class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['recipe_name', 'rating', ]

"""

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', ]

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('amount', 'unit', )
"""

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'meal_type', 'directions', ]
        #if using multiple forms, I will remove some fields i.e.measurement, ingredients, title


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
"""

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'recipe'))
MeasurementFormSet = inlineformset_factory(Ingredient, Measurement, fields=('amount', 'unit', 'ingredient'))