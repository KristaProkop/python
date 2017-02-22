from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    context = {
    'currentdate': datetime.datetime.now().date(),
    'currenttime': datetime.datetime.now().time(),
    }
    return render(request, 'timedisplay/index.html', context)
