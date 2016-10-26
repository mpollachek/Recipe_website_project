from django.contrib import admin

from models import Recipe, Ingredient, MealType, UserProfile



MyModels = [Recipe, Ingredient, MealType, UserProfile]

admin.site.register(MyModels)


