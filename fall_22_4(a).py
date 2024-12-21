# urls.py
urls patterns = [
     path('books/', views.books , name = 'books'),
     path('authors/' , views.authors , name = "authors"),
     path('book2/' , views.add_book , name = 'add_book'),
]

# views.py

from django import BoolForm
from django. shortcuts import render,redirect

def books(request):
     books = book.objects.all()
     return render(request, 'book/books.html',{'books':books})

def authors(request):
     authors= authors.objects.all()
     return render(request, 'book/authors.html', {'authors':authors})

def book2(request):
     book2= book2.onjects.all()
     return render(request, 'book/book2.html', {'book2':book2})

     
