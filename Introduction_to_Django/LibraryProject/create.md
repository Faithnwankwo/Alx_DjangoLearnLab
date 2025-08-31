# Create

from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created:", b.id, str(b))
# Example output:
# Created: 1 1984 by George Orwell (1949)
