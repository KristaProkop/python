from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Author, Book, Review
from ..login.models import User, UserManager



def index(request):
    context = {
        'recent_books': Book.objects.all().order_by('-created_at')[:3],
        'other_books': Book.objects.all().order_by('-created_at')[4:],
        'authors': Author.objects.all(),
        'reviews': Review.objects.all(),
    }
    return render(request, 'book_reviews/index.html', context)

def add_book(request):
    if request.method == "GET":
        context = {
            'authors': Author.objects.all()
        }
        return render(request, 'book_reviews/add_book.html', context)
    else:
        try: 
            author = Author.objects.create_author(request.POST)
            book = Book.objects.create_book(request.POST, author)
            review = Review.objects.create_review(request.POST, book.id, request.session['id'])
            return redirect(reverse('book_reviews:index'))
        except:
            return render(request, 'book_reviews/add_book.html')

def show_book(request, id):
    if request.method == "GET":
        book = Book.objects.get(id=id)
        context = {
            'book': book,
            'author': book.author.name,
            'reviews': Review.objects.filter(book=book)
        }
        return render(request, 'book_reviews/show_book.html', context)

def add_review(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        review = Review.objects.create_review(request.POST, book.id, request.session['id'])
        return redirect(reverse('book_reviews:show_book', kwargs={'id': id})) 
    return redirect(reverse('book_reviews:index'))

def show_user(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
        'reviews': Review.objects.filter(user=user)
    }
    return render(request, 'login/show_user.html', context)

        