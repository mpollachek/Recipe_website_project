from django.conf.urls import url

from recipe_app.views import home, favorites, toprated, myrecipes, addrecipe, signin, createaccount,

urlpatterns = [
    url(r'^$', home),
    url(r'^$', favorites),
    url(r'^$', toprated),
    url(r'^$', myrecipes),
    url(r'^$', addrecipe),
    url(r'^$', signin),
    url(r'^$', createaccount),
    url(r'^$', contact),
    url(r'^$', about),
]