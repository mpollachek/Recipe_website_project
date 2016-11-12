from __future__ import unicode_literals

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models

from star_ratings.models import Rating



RATING_VALUES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


MEASUREMENTUNIT_CHOICES = (('dash', 'dash'), ('tsp', 'tsp'), ('tbsp', 'tbsp'), ('fl oz', 'fl oz'), ('cup', 'cup'),
                           ('pint', 'pint'), ('quart', 'quart'), ('ml', 'ml'), ('cc', 'cc'), ('liter', 'liter'),
                           ('lb', 'lb'), ('oz', 'oz'), ('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('pieces', 'pieces'),
                           ('whole', 'whole'), ('slice', 'slice')
                           )



class MealType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "{}".format(self.name)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    meal_type = models.ForeignKey(MealType)
    directions = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    ratings = GenericRelation(Rating)

    def __unicode__(self):
        return "Recipe: {}, description: {}, meal_type: {}, directions: {}, id: {}"\
            .format(self.recipe_name, self.description, self.meal_type, self.directions, self.id)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={'id': self.id})

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
        return "{} {} {} - {} ".format(self.quantity, self.measurement_unit, self.ingredient_name, self.recipe.recipe_name)



"""
class RecipeRating(models.Model):

    class Meta:
        unique_together = (('recipe_r_name', 'author'))

    recipe_r_name = models.ForeignKey(Recipe)
    rating = models.FloatField(choices=RATING_VALUES, null=True)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "Recipe Name: {}, Recipe Rating: {}, Recipe Author: {}" .format(self.recipe_r_name, self.rating, self.author)
"""


class UserProfile(models.Model):
    if __name__ == '__main__':
        user = models.OneToOneField(User)  #Required-links UserProfile to a User model instance

        #The additional attributes we wish to include:
        #picture = models.ImageField(upload_to='profile_images', blank=True)

        def __unicode__(self):
            return self.user



class Favorite(models.Model):
    fav_recipe = models.ManyToManyField(Recipe)
    fav_user = models.ManyToManyField(User)

    def __str__(self):
            return "recipe: {}, user: {}".format(self.fav_recipe, self.fav_user)
