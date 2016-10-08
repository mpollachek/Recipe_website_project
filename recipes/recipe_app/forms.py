from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from recipe_app.models import Ingredient, Recipe, RecipeRating, UserProfile, MealType, MEALTYPE_CHOICES, Measurement, RecipeName


class RecipeNameForm(forms.Form):
    class Meta:
        model = RecipeName
        fields = ['title', ]

class MealTypeForm(forms.Form):
    mt_field = forms.MultipleChoiceField(choices=MEALTYPE_CHOICES,
                                         widget=forms.CheckboxSelectMultiple())


class SearchRecipeForm(forms.TextInput):
    class Meta:
        model = Recipe
        fields = ['title', 'meal_type', 'ingredients',]


class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['recipe_name', 'rating', ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', ]

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('amount', 'unit', )

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'meal_type', 'measurement', 'ingredients', 'directions', ]
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