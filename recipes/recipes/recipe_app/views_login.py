from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../home')
            else:
                return HttpResponse("Your Baller Recipes account is disabled")

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Your username or password is incorrect")

    else:
        return render(request, 'login.html')