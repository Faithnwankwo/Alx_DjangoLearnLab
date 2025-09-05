from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book, Library
from .forms import SignUpForm

# Home (existing)
def home(request):
    ctx = {"book_count": Book.objects.count(), "library_count": Library.objects.count()}
    return render(request, "relationship_app/home.html", ctx)

# Class-based book list (existing)
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/book_list.html"

# Class-based book detail (existing)
class BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/book_detail.html"

# Create book (existing; requires permission)
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author"]
    permission_required = "relationship_app.add_book"
    template_name = "relationship_app/book_form.html"
    success_url = reverse_lazy("book_list")

# Helper for role check (existing)
def is_librarian(user):
    profile = getattr(user, "profile", None)
    return bool(profile and profile.role in ("LIBRARIAN", "ADMIN"))

# Role-restricted library books (existing)
@login_required
@user_passes_test(is_librarian)
def library_books(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, "relationship_app/library_books.html", {"library": library})

# Signup (existing)
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = getattr(user, "profile", None)
            if profile:
                profile.role = form.cleaned_data["role"]
                profile.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

# ===== NEW FOR THIS TASK =====

# Function-based view: list all books (HTML by default, plain text with ?as=text)
def list_books(request):
    books = Book.objects.select_related("author").all()
    if request.GET.get("as") == "text":
        lines = [f"{b.title} by {b.author.name}" for b in books]
        return HttpResponse("\n".join(lines), content_type="text/plain")
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: details for one library (and its books)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
