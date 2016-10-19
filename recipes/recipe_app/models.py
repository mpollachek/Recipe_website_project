from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth .models import User


RATING_VALUES = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))


MEASUREMENTUNIT_CHOICES = (('tsp', 'tsp'), ('tbsp', 'tbsp'), ('fl oz', 'fl oz'), ('cup', 'cup'), ('pint', 'pint'),
                           ('quart', 'quart'), ('ml', 'ml'), ('cc', 'cc'), ('liter', 'liter'), ('lb', 'lb'),
                           ('oz', 'oz'), ('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('pieces', 'pieces'))



class MealType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "{}".format(self.name)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    meal_type = models.ForeignKey(MealType)
    directions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Recipe {}, description: {}, meal_type: {}, directions: {}"\
            .format(self.recipe_name, self.description, self.meal_type, self.directions)

    def get_rating(self):
        if not self.rating_set.count():
            return "No ratings for {}" .format(self.recipe_name)
        total = 0
        for rate in self.rating_set.all():
            total += rate.rating
        return total / self.rating_set.count()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient_name = models.CharField(max_length=255)
    quantity = models.FloatField(max_length=10)
    measurement_unit = models.CharField(max_length=100, choices=MEASUREMENTUNIT_CHOICES, null=True)

    def __unicode__(self):
        return "{} {} - {}".format(self.quantity, self.measurement_unit, self.ingredient_name, self.recipe)


class RecipeRating(models.Model):
    recipe = models.ForeignKey(Recipe)
    rating = models.FloatField(choices=RATING_VALUES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """
    def __unicode__(self):
        return "RecipeRating"
    """


class UserProfile(models.Model):
    if __name__ == '__main__':
        user = models.OneToOneField(User)  #Required-links UserProfile to a User model instance

        #The additional attributes we wish to include:
        #picture = models.ImageField(upload_to='profile_images', blank=True)

        def __unicode__(self):
            return self.user.username