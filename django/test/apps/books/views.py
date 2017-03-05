# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
# from .models import Secret, SecretManager, Like, LikeManager
from ..login.models import User, UserManager

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    else: 
        return render(request, 'books/index.html')

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))