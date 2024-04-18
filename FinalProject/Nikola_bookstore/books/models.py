from django.db import models

class BookManager(models.Manager):
    def get_books_for_homepage(self):
        return self.all()[:5] # Returns the first 5 books
    
    def get_book_by_id(self, book_id):
        return self.get(id=book_id) #returns one book

# Create your models here.
#Create book model with attributes title, author, year, rating, and description

class Book(models.Model):
    # Attribute to store book title as Char field
    title = models.TextField(max_length=200)
    #Attruibute to store author
    author = models.TextField(max_length=200)
    # att to store year
    year = models.TextField(max_length=200)
    
    rating = models.TextField(max_length=200)
    
    description = models.TextField(max_length=200)
    
    objects = BookManager()
    
    # Override string repsentation of object
    def __self__(self): 
        # Return book title when printing book model
        return self.title
