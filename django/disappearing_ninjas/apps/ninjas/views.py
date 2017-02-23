from django.shortcuts import render, redirect

def index(request):
    return render(request, 'ninjas/index.html')

# def show_all(request):
#     context = {
#         'color': 'all'
#     }
#     return render(request, 'ninjas/ninja.html', context)

def show(request, *color):
    if color:
        context = {
            'color': color,
        }
    else:
        context = {
            'color': 'all',
        }
    return render(request, 'ninjas/ninja.html', context)



