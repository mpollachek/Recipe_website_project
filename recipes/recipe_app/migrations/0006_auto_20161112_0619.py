# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='fav_recipe',
            field=models.ManyToManyField(to='recipe_app.Recipe'),
        ),
    ]