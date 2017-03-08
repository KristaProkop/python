from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse


def index(request):
    request.session['id'] = 1
    if 'id' not in request.session:
        return redirect(reverse('loginReg:index'))
    else:
        context = {
        'users': {
            'id': 1, 
            'name': 'krista', 
            'email': 'krista@mail', 
            'creted_at': 'blah', 
            'level': 9,
            }
        }
        return render(request, 'dashboard/dashboard.html', context)

def add_user(request):
    return render(request, 'dashboard/add_user.html')

def edit_user(request):
    return render(request, 'dashboard/update_profile.html')

def show_user(request):
    return render(request, 'dashboard/show_user.html')