from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from forms import UserForm #UserProfileForm


def createaccount(request):

    #Boolean value telling template whether registration was successfull
    #set to false initially.  Code changes value to True when registration succeeds
    registered = False

    if request.method == 'POST':
        #grab info from form
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid():
        #and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            #profile = profile_form.save(commit=false)
            #profile.user = user

            #if 'picture' in request.FILES:
                #profile.picture - request.FILES['picture']

            #profile.save()

            registered = True

    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    context = {'user_form': user_form, 'registered': registered}

    #if I use profile_form, I must add 'profile_form': profile_form
    return render(request, 'createaccount.html', context)
