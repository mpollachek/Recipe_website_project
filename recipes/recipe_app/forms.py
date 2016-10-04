from django import forms
from django.contrib.auth.models import User

from recipe_app.models import Ingredient, Recipe, RecipeRating, UserProfile


class SearchRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'meal_type', 'ingredients',]


class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['recipe_name', 'rating',]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', ]

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'meal_type', 'measurement', 'ingredients', 'directions',]


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