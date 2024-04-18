from django.contrib import admin
from django.urls import path, include
from . import views

#_homepage
#_detail
urlpatterns = [
   path ('', views.books, name="books"), # all books BOOKS
   #path('book/', views.books, name="books"),
   path ('book/<str:pk>/', views.book, name="book" ) ,# detial book one book BOOK
   
    # Route to add book using form
   path ('addbook/', views.addBook, name='addBook'),
   
   # Route to edit book using form
    path('editbook/<str:pk>/', views.editBook, name="editBook"),
    
     # Route to delete book
    path ('deletebook/<str:pk>/', views.deleteBook, name="deleteBook"),
    
]

    
   
   
  

