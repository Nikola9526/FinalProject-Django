from django.shortcuts import render

# Create your views here.

books_array = [
    {"id": "1", "title":"Mongo", "author": "Nikola", "year": "2014", "rating": "5/5", "description": "About Mongo"},
    {"id": "2", "title":"Python", "author": "Nikola","year": "2014", "rating": "5/5", "description": "About Mongo"}
    
]

def book(request):
     # Create object to store movie
   
    context ={
        "page_title": "Books",
        "books_array": books_array,
        "page_author": "Niki"
    }
    
    return render (request, "home_page.html", context)




def books(request, pk):
     # Create object to store movie
    book = None
    # Search through all movies for one where id matches pk
    for book_index in books_array:
        # check to see if pk matches movie int
        if pk == str(book_index.get('id')):
            # Set movie to movie with matchin id from movies
            book = book_index

    
    
    context ={
        "page_title": "Books",
        "books":book,
        "page_author": "Niki"
    }
    
    return render (request, "book_page.html", context)