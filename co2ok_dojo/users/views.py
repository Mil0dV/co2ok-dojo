from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404


from wagtail.core.models import Page
from wagtail.search.models import Query

#from .forms import LoginForm
from .forms import RegisterForm
#from .models import Profil


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            #form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username, email, password)
            #Profil.objects.create(point=0, uniq_link=request.user.id)
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('/{0}'.format(user.id))
    else:
        form = RegisterForm()

    #return render(request,'users/login.html',{'form': register_form})
    return render(request, 'users/login.html', {'form': form})



# def login(request):
#
#     if request.method == "POST":
#
#         login_form = LoginForm(request.POST or None)
#         if login_form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 redirect('/profile')
#             else:
#                 error:true
#
#     else:
#        form: LoginForm()
#
#     return render(request,'users/login.html')


def profil(request, id):
    # username = request.user
    # password = request.user.password
    user_id = request.user.id
    if int(id) == int(user_id):
        return render(request,'users/profile.html',{'id':id, 'current_path': request.get_full_path()})
    else:
        #return HttpResponse('you are not connected! {0}'.format(user_id))
        #return redirect('/{0}'.format(id))
        form = RegisterForm(request.POST)
        return render(request, 'users/invited_sign_page.html', {'userid': id, 'form': form})


def invited_sign(request, user_id):
    return render('users/invited_sign_page.html',{'username': request.user.username})
