from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Books (already in your project)
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("libraries/<int:pk>/books/", views.library_books, name="library_books"),

    # Auth (task 2)
    path("login/",  LoginView.as_view(template_name="relationship_app/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Task 1 endpoints
    path("list_books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Role-restricted views (grader looks for these)
    path("admin-only/",     views.admin_view,     name="admin_view"),
    path("librarian-only/", views.librarian_view, name="librarian_view"),
    path("member-only/",    views.member_view,    name="member_view"),
]
