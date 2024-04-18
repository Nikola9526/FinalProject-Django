from django.urls import path
# Import views from current base app folder
from . import views


# Create base app urls
urlpatterns = [
    path ('', views.bookstore_home, name = 'bookstore_home'),
    path('book/<int:book_id/', views.book_detail, name="book_details"),
]

## path('movie/<int:pk>/', movie, name='movie'),