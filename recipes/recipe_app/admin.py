from django.contrib import admin

from models import Recipe, Ingredient, Measurement, RecipeRating, MealType


MyModels = [Recipe, Ingredient, Measurement, RecipeRating, MealType]

admin.site.register(MyModels)


