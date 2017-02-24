from django.shortcuts import render
from .models import User, Post

def index(request):
    People.objects.create(first_name="me", last_name="mine")
    people = People.objects.all()
    print (people)
    return render(request, 'third_app/index.html') 