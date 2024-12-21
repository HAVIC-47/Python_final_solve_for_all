from django import forms
from .models import author,book

class BookFrom(forms.ModelForm):
     class Meta:
          model = book
          fiels = ['name','genre','publication','author']

# view.py

from djanngo import BookFrom
from django.shortcuts import render,redirect

def add_book(request):
     if request.method == "POST":
          from = BookFrom(request.POST)
          if form.is_valid():
               from.save()
               return redirect('home')
     else:
          from = Bookform()
     return render(request, 'book/add_book.html',{'form':form})

# add_book.html
<!DOCTYPE html>
<html>
<head>
    <title>Add Book</title>
</head>
<body>
    <h1>Add a New Book</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
