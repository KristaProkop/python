from django.shortcuts import render, redirect
from .models import Product
from django.core.urlresolvers import reverse
from django.contrib import messages


def index(request):
    context = {
        'products': Product.objects.all().order_by('name')
    }
    return render(request, 'restful/index.html', context)

def destroy(request, id):
    if request.method=="POST":
        Product.objects.get(id=id).delete()
        messages.success(request, "Product successfully deleted")
    return redirect(reverse('restful:index'))

def show(request, id):
    context = {
            'product': Product.objects.get(id=id)
        }
    return render(request, 'restful/show.html', context)

def new(request):
    return render(request, 'restful/new_product.html')

def create(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        price = float(request.POST['price'])
        Product.objects.create(name=name, description=description, price=price,
            )
    return redirect(reverse('restful:index'))

def edit(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'restful/edit_product.html', context)

def update(request, id):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        price = float(request.POST['price'])
        Product.objects.filter(id=id).update(name=name, description=description, price=price)
    return redirect(reverse('restful:index'))


