from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Secret, SecretManager
from ..login.models import User, UserManager
# Create your views here.
def index(request):
    Secret.objects.create_secret(user_id=1, message="test message")
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    else: 
        context = {
            'secrets': Secret.objects.all().order_by('created_at')[:10],
        }
        return render(request, 'secrets/index.html', context)

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

def most_popular(request):
    context = {
        'secrets': Secret.objects.all().order_by('created_at'),
    }
    return render(request, 'secrets/popular_secrets.html', context)

def create_secret(request, id):
    Secret.objects.create_secret(message=request.POST['message'], user_id=id)
    return redirect(reverse('secrets:index'))

def delete_secret(request, id):
    Secret.objects.delete_secret(secret_id=id)
    return redirect(reverse('secrets:index'))


def create_like(request, user_id, secret_id):
    print user_id, secret_id
    Secret.objects.create_like(user_id=user_id, secret_id=secret_id)
    return redirect(reverse('secrets:index'))

