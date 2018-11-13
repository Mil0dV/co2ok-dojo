from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from cuser.forms import UserCreationForm

# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages


from wagtail.core.models import Page
from wagtail.search.models import Query

from .forms import RegisterForm, LoginForm
from .models import Rewards


def register(request):
    cuser = get_user_model()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            #form.save()
            #username = form.cleaned_data['username']
            # username = 'random'
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_email_count = cuser.objects.filter(email=email).count()
            if user_email_count == 0:
                cuser.objects.create_user(email, password)
                user = authenticate(email=email, password=password)
                Rewards.objects.create(user_id=user.id, points=0)
                login(request, user)
                # return redirect('/{0}'.format(user.id))
                return redirect('/accounts/profile')
            else:
                messages.error(request, "This email already exist")
    else:
        messages.error(request, 'Form not valid')
        form = RegisterForm()

    #return render(request,'users/login.html',{'form': register_form})
    return render(request, 'registration/register.html', {'form': form})



# def login(request):
#
#     if request.method == "POST":
#
#         login_form = LoginForm(request.POST)
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
#     return render(request,'users/login.html', {'login_form': login_form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# def home(request):
#     return render(request, 'core/home.html')


@login_required
def profile(request):
    # username = request.user
    # password = request.user.password
    user_id = request.user.id
    # if int(id) == int(user_id):
    try: 
        user_points = Rewards.objects.get(user_id = user_id).points 
    except:
        user_points = 9042
    profile_data = {

      'current_path': user_id,
      'user_points': user_points

    }
    return render(request,'users/profile.html', profile_data)
    # else:
    #     #return HttpResponse('you are not connected! {0}'.format(user_id))
    #     #return redirect('/{0}'.format(id))
    #     form = RegisterForm(request.POST)
    #     return render(request, 'users/invited_sign_page.html', {'userid': id, 'form': form})


def invited_sign(request, user_id):
    cuser = get_user_model()
    user_who_invite_id = cuser.objects.get(id=user_id)
    form = RegisterForm(request.POST)
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            #form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_email_count = cuser.objects.filter(email=email).count()
            if user_email_count == 0:
                cuser.objects.create_user(email, password)
                invited_user = authenticate(email=email, password=password)
                Rewards.objects.create(user_id=invited_user.id, points=0)
                print('updated_user_who_invite_points' + updated_user_who_invite_points)
                #updating user points
                user_who_invite_points = Rewards.objects.get(user_id=user_id).points
                updated_user_who_invite_points = user_who_invite_points + 1
                Rewards.objects.filter(user_id=user_id).update(points=updated_user_who_invite_points)
                print('updated_user_who_invite_points' + updated_user_who_invite_points)
                login(request, invited_user)
                return redirect('/accounts/profile')
    else:
        #messages.error(request, 'Form not valid')
        form = RegisterForm()

    user_obj = {

     'email':user_who_invite_id.email,
     'user_id': user_id,
     'form': form

    }
    return render(request,'users/invited_sign_page.html', user_obj)
