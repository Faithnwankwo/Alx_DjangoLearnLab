from django.urls import path
from django.contrib.auth import views as auth_views
from . import views                       # <-- keep this so we can use views.register
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Existing views
    path("", views.home, name="home"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("libraries/<int:pk>/books/", views.library_books, name="library_books"),

    # Authentication (built-in + your register view)
    path("login/",  auth_views.LoginView.as_view(template_name="relationship_app/login.html"),  name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),   # <-- REQUIRED STRING

    # Task 1 canonical routes
    path("list_books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Aliases kept
    path("fb/books/", views.list_books, name="list_books_fb"),
    path("cb/library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail_cb"),

    # Existing custom signup
    path("accounts/signup/", views.signup, name="signup"),
]
