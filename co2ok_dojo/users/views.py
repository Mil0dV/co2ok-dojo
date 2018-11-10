from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
# from django.contrib import messages


from wagtail.core.models import Page
from wagtail.search.models import Query

#from .forms import LoginForm
from .forms import RegisterForm
from .models import Rewards


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
            Rewards.objects.create(user_id=user.id, points=0)
            login(request, user)
            # return redirect('/{0}'.format(user.id))
            return redirect('/profil')
    else:
        #messages.error(request, 'Form not valid')
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


def profil(request):
    # username = request.user
    # password = request.user.password
    user_id = request.user.id
    # if int(id) == int(user_id):
    user_points = Rewards.objects.get(user_id = int(request.user.id)).points
    profil_data = {

      'current_path': user_id,
      'user_points': user_points

    }
    return render(request,'users/profile.html', profil_data)
    # else:
    #     #return HttpResponse('you are not connected! {0}'.format(user_id))
    #     #return redirect('/{0}'.format(id))
    #     form = RegisterForm(request.POST)
    #     return render(request, 'users/invited_sign_page.html', {'userid': id, 'form': form})


def invited_sign(request, user_id):
    current_user = User.objects.get(id=user_id)
    form = RegisterForm(request.POST)
    user_obj = {

     'username':current_user.username,
     'user_id': user_id,
     'form': form

    }
    return render(request,'users/invited_sign_page.html', user_obj)
