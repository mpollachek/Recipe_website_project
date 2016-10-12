from django.contrib import admin

from models import Recipe, Ingredient, RecipeRating, MealType, UserProfile


MyModels = [Recipe, Ingredient, RecipeRating, MealType, UserProfile]

admin.site.register(MyModels)


