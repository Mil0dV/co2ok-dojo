from django.shortcuts import render
from users.models import *

# Create your views here.

def welcome(request):
    userid = request.user.id
    Profile.objects.filter(user__pk=userid).update(ninja_user=True)
    return render(request,'welcome/welcome.html',{'userid':userid})
