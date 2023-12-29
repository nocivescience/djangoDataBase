from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
def book_list(request):
    return render(request, 'myapp/book_list.html')