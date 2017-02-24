from django.shortcuts import render
from .models import User, Message, Comment

# Create your views here.
def index(request):
    User.objects.create(first_name="krista", last_name="Prokopczyk", email="krista@mail.com", password="blah" )
    krista = User.objects.all()
    print krista
    return render(request, 'wall/index.html')
