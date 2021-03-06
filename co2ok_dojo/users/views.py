from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from cuser.forms import UserCreationForm
import random
# from django.contrib.gis.geoip2 import GeoIP2
# from django.utils import translation

# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.utils.translation import ugettext as _


from wagtail.core.models import Page
from wagtail.search.models import Query

from .forms import RegisterForm, LoginForm
from .models import Profile


def signup(request):
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
                Profile.objects.create(user=user, points=0, user_picked_project=0)
                login(request, user)
                # return redirect('/{0}'.format(user.id))
                return redirect('/accounts/profile')
            else:
                messages.error(request, "This email already exist")
    else:
        messages.error(request, '')
        form = RegisterForm()

    #return render(request,'users/login.html',{'form': register_form})
    return render(request, 'registration/register.html', {'form': form, 'full_path': request.get_full_path()})



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
    trans = _("mot a traduire")
    # picked_project = request.GET.get('causePicked')
    # if picked_project != None:
    #     picked_project = request.GET.get('causePicked')
    # else:
    #     picked_project = ''

    # if int(id) == int(user_id):
    try:
        user_points = Profile.objects.get(user__pk = user_id).points
        user_app = Profile.objects.get(user__pk = user_id).ninja_user
        user_project = Profile.objects.get(user__pk = user_id).user_picked_project
    except:
        user_points = 9042
        user_app = False
        user_project = 0

    profile_data = {

      'current_path': user_id,
      'user_points': user_points,
      'trans': trans,
      'user_id': user_id,
      'user_project': user_project,
      'user_app': user_app,
      # Milo: ik denk dat de strip niet nodig is. YOLO 'm weg als je je dapper voelt, maar test wel op productie :P
      'domainname': request.get_host() if request.get_host().strip() else 'test.co2ok.ninja'

    }
    return render(request,'users/profile.html', profile_data)



def picked_cause(request):
    picked_project = request.GET.get('causePicked')
    user_id = request.user.id
    user_pickedproject = Profile.objects.filter(user__pk = user_id).update(user_picked_project=picked_project)
    # user_project = Profile.objects.get(user__pk = user_id).email
    return render(request, 'ajax_data.html',{'picked_project': picked_project})


def invited_sign(request, user_id):
    cuser = get_user_model()
    user_who_invite_id = cuser.objects.get(id=user_id)
    form = RegisterForm(request.POST)
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_email_count = cuser.objects.filter(email=email).count()
            if user_email_count == 0:
                cuser.objects.create_user(email, password)
                invited_user = authenticate(email=email, password=password)
                Profile.objects.create(user=invited_user, points=0)
                #updating user points
                user_who_invite_points = Profile.objects.get(user__pk=user_id).points
                updated_user_who_invite_points = user_who_invite_points + 1
                Profile.objects.filter(user__pk=user_id).update(points=updated_user_who_invite_points)
                login(request, invited_user)
                return redirect('/accounts/profile')
    else:
        messages.error(request, '')
        form = RegisterForm()

    user_obj = {

     'email':user_who_invite_id.email,
     'user_id': user_id,
     'form': form

    }
    return render(request,'users/invited_sign_page.html', user_obj)

def pick_a_project(request):
    user_picked_project = 'biogasInstallation'
    x = request.POST['co2ok_pick_project_button']
    # user_picked_project = co2ok_pick_project_button

    if x == 'biogasInstallation':
        user_picked_project = 'biogasInstallation'
    elif x == 'solarPanel':
        user_picked_project = 'solarPanel'
    elif x == 'save80cookingStove':
        user_picked_project = 'save80cookingStove'
