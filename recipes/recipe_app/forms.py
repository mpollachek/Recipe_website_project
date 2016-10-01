from django import forms

from recipe_app.models import RecipeRating


class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['recipe_name', 'rating',]