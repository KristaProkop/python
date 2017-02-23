from django.shortcuts import render, redirect


def index(request):
    return render(request, 'ninjas/index.html')

def show(request, color=None):
    if color:
        context = {
            'color': color,
        }
    else:
        context = {
            'color': 'all',
        }
    return render(request, 'ninjas/ninja.html', context)



