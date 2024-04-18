from django.shortcuts import render, get_object_or_404
from .models import Book

# Create books object array
books_array = [
    {"id": 1, "title": "Monthy Python and the Holy Grail", "author": "Nikola"},
    {"id": 2, "title": "The Lion King", "author": "Ti"},
    {"id": 3, "title": "Pirates of the Carribean", "author": "R"}
]

# Create your views here.

def book_detail(request, book_id):
    book = get_object_or_404(Book,pk=book_id)
    return render (request, 'books/book_detail.html', {'book': book})
