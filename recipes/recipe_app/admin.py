from django.contrib import admin

from models import Recipe, Ingredient, MealType, UserProfile, Favorite



MyModels = [Recipe, Ingredient, MealType, UserProfile, Favorite]

admin.site.register(MyModels)


