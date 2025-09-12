from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def home(request):
    return HttpResponse("✅ Welcome to the Library home page!")

def books_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'catalog/books_list.html', {'books': books})


