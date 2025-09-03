from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book, Library
from .forms import SignUpForm

def home(request):
    ctx = {"book_count": Book.objects.count(), "library_count": Library.objects.count()}
    return render(request, "relationship_app/home.html", ctx)

class BookListView(ListView):
    model = Book
    template_name = "relationship_app/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/book_detail.html"

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author"]
    permission_required = "relationship_app.add_book"
    template_name = "relationship_app/book_form.html"
    success_url = reverse_lazy("book_list")

def is_librarian(user):
    profile = getattr(user, "profile", None)
    return bool(profile and profile.role in ("LIBRARIAN", "ADMIN"))

@login_required
@user_passes_test(is_librarian)
def library_books(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, "relationship_app/library_books.html", {"library": library})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # profile created by signal
            profile = getattr(user, "profile", None)
            if profile:
                profile.role = form.cleaned_data["role"]
                profile.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
