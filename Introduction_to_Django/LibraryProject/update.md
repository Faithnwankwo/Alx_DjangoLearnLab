# Update

from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print("Updated title:", book.title)
# Example output:
# Updated title: Nineteen Eighty-Four
