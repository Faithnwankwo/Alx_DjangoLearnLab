from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book
# === Task 4: permission-protected Book views ===
@permission_required("relationship_app.can_add_book")
def add_book_view(request):
    return HttpResponse("Add book page (requires can_add_book)")

@permission_required("relationship_app.can_change_book")
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Edit book page for '{book.title}' (requires can_change_book)")

@permission_required("relationship_app.can_delete_book")
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Delete book page for '{book.title}' (requires can_delete_book)")
