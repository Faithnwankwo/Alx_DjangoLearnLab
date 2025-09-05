from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("libraries/<int:pk>/books/", views.library_books, name="library_books"),
    path("accounts/signup/", views.signup, name="signup"),

    # New for Task 1
    path("fb/books/", views.list_books, name="list_books_fb"),
    path("cb/library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail_cb"),
]
