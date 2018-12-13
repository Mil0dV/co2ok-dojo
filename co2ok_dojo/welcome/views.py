from django.shortcuts import render

# Create your views here.

def welcome(request):
    user = request.user.email
    return render(request,'welcome/welcome.html',{'userid':user})
