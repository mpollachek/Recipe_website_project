from django.conf.urls import url

from recipe_app.views import home, favorites, toprated, myrecipes, contact, about

from recipe_app.views_create_account import createaccount
from recipe_app.views_login import user_login
from recipe_app.views_logout import user_logout
from recipe_app.views_addrecipe import addrecipe

urlpatterns = [
    url(r'^home/$', home),
    url(r'^favorites/', favorites),
    url(r'^toprated/', toprated),
    url(r'^myrecipes/', myrecipes),
    url(r'^addrecipe/', addrecipe),
    url(r'^createaccount/', createaccount),
    url(r'^contact/', contact),
    url(r'^about/', about),
    url(r'^login/', user_login),
    url(r'^logout/', user_logout),
]