from django.shortcuts import render
from users.models import *

# Create your views here.

def welcome(request):
    userid = request.user.id
    Profile.objects.filter(user__pk=userid).update(ninja_user=True)
    user_app = Profile.objects.get(user__pk=userid).ninja_user
    return render(request,'welcome/welcome.html',{'userid':userid, 'user_app': user_app})
