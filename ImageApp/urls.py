from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name = 'home'),
    path('hate',views.BookCreate,name='jack'),
    path('book-list/',views.BookListView,name = 'book-list'),
    path('book-detail/<int:pk>/',views.BookDetailView,name = 'book-detail'),
    path('book-update/<int:pk>/',views.BookUpdateView,name = 'book-update'),
    path('book-delete/<int:pk>/',views.BookDeleteView,name = 'book-delete'),

]