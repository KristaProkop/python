from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')


def process(request):
    if request.method == 'POST':
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('result.html')
    else: 
        return redirect('/')

def create(request):
    return render(request,'survey/result.html')

def home(request):
    return redirect('/')
