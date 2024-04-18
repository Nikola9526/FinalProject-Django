from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
#from .forms import BookForm 

# Create your views here.

def books_homepage(request):
    context ={
        "page_title": "Welcome to Our Bookstore",
        "page_subtitle": "Featured Books",
        "page_author": "Nikola"
    }
    books = Book.objects.get_books_for_homepage()
    return render(request, 'home_page.html', {'books': books}, context)


def book_detail (request, book_id):
    context ={
        "page_title": "Book Selected",
        
        }
    
    book = Book.objects.get_book_by_id(book_id)
    return render(request, 'book_page.html', {'book': book},context)


#to addBook to DB
def addBook(request):
    # Create movie form object
    #form = BookForm()
    # When form submitted
    if request.method == 'POST':
        # Create movie object from form
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            year=request.POST.get('year'),
            rating= request.POST.get('rating'),
            description=request.POST.get('description'),
            
            
        )
        # Redirect to homepage
        return redirect('/')

    context = {'book': book}
    return render(request, 'book_form.html', context)


# View to update Book in DB
def editBook(request, pk):
    # Get book object from db with id by using model
    book = Book.objects.get(id=pk)
    # Generate Movieform for movie
    #form = BookForm(instance=book)

    # User need to be logged in as well as
    # The user that posted the book
    if request.user != book.posted_by:
        return render(request, "not_authorized.html")

    # When form submitted get values
    if request.method == 'POST':
        # Update model based on form values
        book.title = request.POST.get('title')
        book.author= request.POST.get('author')
        book.year = request.POST.get('year')
        book.rating = request.POST.get('rating')
        book.description = request.POST('description')
        # Save model in db
        book.save()
        # Redirect to home
        return redirect('/')

    # Return and render movie form
    context = { 'book': book}
    return render(request, 'book_form.html', context)


# View to Delete Book in DB
def deleteBook(request, pk):
    # Get movie object from db using model
    book = Book.objects.get(id=pk)

    # User need to be logged in as well as
    # The user that posted the book
    if request.user != book.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        # Delete movie object and dbs
        book.delete()
        # Return home
        return redirect('/')
    # Render confirm delete page
    return render(request, 'delete.html', {'obj': book})


books_array = [
    {"id": 1, "title":"Mongo", "author": "Nikola", "year": "2014", "rating": "5/5", "description": "About Mongo"},
    {"id": 2, "title":"Python", "author": "Nikola","year": "2014", "rating": "4/5", "description": "Python Basics"},
    {"id": 3, "title":"Intro to Javascript", "author": "Bill","year": "2020", "rating": "4.9/5", "description": "Javascript Basics"},
     {"id": 4, "title":"Intro to  Linux", "author": "Sam","year": "2022", "rating": "4.7/5", "description": "Linux and Shell Basics"},
      {"id": 5, "title":"Intro to Java", "author": "Niki","year": "2014", "rating": "4.4/5", "description": "Java Basics"},
    
]
#multiple book viewings home_page.html
def books(request):
     # Create object to store movie
   
    context ={
        "page_title": "Books",
        "books_array": books_array,
        "page_author": "Niki"
    }
    
    return render (request, "home_page.html", context)

#single book viewing book_page.html
def book(request, pk):
     # Create object to store movie
    book = None
    # Search through all movies for one where id matches pk
    for book_index in books_array:
        # check to see if pk matches movie int
        if pk == str(book_index.get('id')):
            # Set movie to movie with matchin id from movies
            book = book_index
    context ={
        "page_title": "Book Details",
        "book":book,
        "page_author": "Niki"
    }
    
    return render (request, "book_page.html", context)