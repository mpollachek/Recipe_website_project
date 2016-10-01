from __future__ import unicode_literals

from datetime import datetime
from django.db import models


RATING_VALUES = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), )

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    meal_type = models.ManyToManyField(MealType)
    measurement = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

"""
    def __unicode__(self):
        return "Recipe {} rating is" .format(self.title)
"""

    def get_rating(self):
        if not self.rating_set.count():
            return "No ratings for {}" .format(self.title)
        total = 0
        for rate in self.rating_set.all():
            total += rate.rating
        return total / self.rating_set.count()

class MealType:
    name = models.CharField(max_length=255)

class Ingredient (models.Model):
    name = models.CharField(max_length=255)

class RecipeRating (models.Model):
    recipe_name = models.ForeignKey(Recipe):
    rating = models.FloatField(choices = RATING_VALUES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """
    def __unicode__(self):
        return "RecipeRating
    """

