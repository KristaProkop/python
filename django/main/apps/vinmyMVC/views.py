from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'email': 'blog@gmail.com',
        'name': 'mike',
    }
    return render(request, 'vinmyMVC/index.html', context)

def show(request):
    print (request.method)
    return render(request, 'vinmyMVC/show_users.html')

def see(request, id):
    context = {
        'id': id,
    }
    return render(request, 'vinmyVMC/see.html')

def create(request):
    print request.method
    if request.method == 'POST':
        print ('*'*50)
        print (request.POST)
        print ('*'*50)
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else: 
        return redirect('/')