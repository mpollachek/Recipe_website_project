from django.conf.urls import url

from recipe_app.views import home, favorites, toprated, myrecipes, contact, about, recipe_detail, recipe_update, recipe_delete

from recipe_app.views_create_account import createaccount
from recipe_app.views_login import user_login
from recipe_app.views_logout import user_logout
from recipe_app.views_addrecipe import addrecipe

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^recipe_detail/(?P<id>\d+)/$', recipe_detail, name='detail'),
    url(r'^recipe_update/(?P<id>\d+)/$', recipe_update, name='update'),
    url(r'^recipe_delete/(?P<id>\d+)/$', recipe_delete, name='delete'),
    url(r'^favorites/', favorites, name='favorites'),
    url(r'^toprated/', toprated, name='toprated'),
    url(r'^myrecipes/', myrecipes, name='myrecipes'),
    #url(r'^addrecipe/', addrecipe, name='addrecipe'),
    url(r'^addrecipe/(?P<recipe_pk>.*)/$', addrecipe, name='addrecipe'),
    url(r'^createaccount/', createaccount, name='createaccount'),
    url(r'^contact/', contact, name='contact'),
    url(r'^about/', about, name='about'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
]