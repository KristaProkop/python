from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Secret, SecretManager, Like, LikeManager
from ..login.models import User, UserManager
# Create your views here.
def index(request):
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    else: 
        context = {
            'secrets': Secret.objects.all().order_by('created_at')[:10],
            'likes': Like.objects.all(),
        }
        return render(request, 'secrets/index.html', context)

def most_popular(request):
    context = {
        'secrets': Secret.objects.all().order_by('created_at'),
        'likes': Like.objects.all(),
    }
    return render(request, 'secrets/popular_secrets.html', context)

def create_secret(request, id):
    Secret.SecretManager.create_secret(message=request.POST['message'], user_id=id)
    return redirect(reverse('secrets:index'))

def delete_secret(request, id):
    Secret.SecretManager.delete_secret(secret_id=id)
    return redirect(reverse('secrets:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

def create_like(request, user_id, message_id):
    Like.LikeManager.create_like(user_id=user_id, message_id=message_id)
    return redirect(reverse('secrets:index'))