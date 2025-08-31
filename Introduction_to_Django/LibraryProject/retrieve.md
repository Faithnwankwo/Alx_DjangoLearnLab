# Retrieve

from bookshelf.models import Book
book = Book.objects.get(id=1)  # or use your actual id
print("Retrieved:", book.id, book.title, book.author, book.publication_year)
# Example output:
# Retrieved: 1 1984 George Orwell 1949

