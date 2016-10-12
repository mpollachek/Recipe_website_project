from recipe_app.models import *

def populate_db(rec=3):
    count=0
    while count < rec:
        x = MealType(name='Breakfast')
        y = MealType(name='Lunch')
        z = MealType(name='Dinner')
        x.save()
        y.save()
        z.save()
        a = Recipe(name='mozz', description='yummy', meal_type=x, directions='eat it')
        a.save()
        b = Recipe(name='guac', description='green', meal_type=y, directions='make it')
        b.save()
        c = Recipe(name='salad', description='healthy', meal_type=z, directions='toss it')
        c.save()
        d = Ingredient(recipe=a, name='mozzerella', quantity=2.5, measurement_unit='lb')
        e = Ingredient(recipe=b, name='avacado', quantity=4.5, measurement_unit='oz')
        f = Ingredient(recipe=c, name='lettuce', quantity=1, measurement_unit='pieces')
        d.save()
        e.save()
        f.save()
        count += 1
