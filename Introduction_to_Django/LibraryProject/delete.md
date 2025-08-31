# Delete

from bookshelf.models import Book
deleted, _ = Book.objects.filter(id=1).delete()
print("Remaining books:", Book.objects.count())
# Example output:
# Remaining books: 0
