from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    # user_lang = 'de';
    # translation.activate(user_lang)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_lang
    return render(request, 'core/home.html')
