from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path ('', views.book, name="books"),
   path('book/', views.book, name="book"),
   path ('books/<str:pk>/', views.books, name="books" )
]