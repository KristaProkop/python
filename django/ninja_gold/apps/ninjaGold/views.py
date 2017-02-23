from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    return render(request, 'ninjaGold/index.html')

def process_money(request):
    if request.method == 'POST':
        if 'counter' not in request.session:
            request.session['counter'] = 0
        request.session['building'] = request.POST['building']
        if request.session['building'] == 'farm':
            award = random.randrange(10, 21) 
        elif request.session['building'] == 'cave':
            award = random.randrange(5, 11) 
        elif request.session['building'] == 'house':
            award = random.randrange(2, 6) 
        elif request.session['building'] == 'casino':
            award = random.randrange(-50, 51) 
        else: 
            print "Something went wrong"
            award = 0
        request.session['counter'] += award
        if 'awards' not in request.session:
            request.session['awards'] = [award]
        request.session['awards'].append(award)
        return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session['counter'] = 0
        request.session['awards'] = []
    return redirect('/')