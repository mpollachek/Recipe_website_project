from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth .models import User


RATING_VALUES = ((1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5))

MEALTYPE_CHOICES = (('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Appetizer', 'Appetizer'),
                    ('Side_Dish', 'Side Dish'), ('Dessert', 'Dessert'))


class RecipeName(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class MealType(models.Model):
    name = models.CharField(max_length=100, choices=MEALTYPE_CHOICES)

    def __unicode__(self):
        return "{}".format(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "{}".format(self.name)

class Measurement(models.Model):
    amount = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)

    def __unicode__(self):
        return "{} {}".format(self.amount, self.unit)

class Recipe(models.Model):
    title = models.ManyToManyField(RecipeName)
    description = models.TextField(null=True)
    meal_type = models.ManyToManyField(MealType)
    measurement = models.ManyToManyField(Measurement)
    ingredients = models.ManyToManyField(Ingredient)
    directions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Recipe {}, description: {}, meal_type: {}, measurement: {}, ingredients: {}, directions: {}"\
            .format(self.title, self.description, self.meal_type, self.measurement, self.ingredients, self.directions)

    def get_rating(self):
        if not self.rating_set.count():
            return "No ratings for {}" .format(self.title)
        total = 0
        for rate in self.rating_set.all():
            total += rate.rating
        return total / self.rating_set.count()

class RecipeRating(models.Model):
    recipe_name = models.ForeignKey(Recipe)
    rating = models.FloatField(choices = RATING_VALUES)
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