# Create

`python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created:", b.id, str(b))
# Example output:
# Created: 1 1984 by George Orwell (1949)


`powershell
# retrieve.md
@"
# Retrieve

`python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print("Retrieved:", book.id, book.title, book.author, book.publication_year)
# Example output:
# Retrieved: 1 1984 George Orwell 1949


`powershell
# update.md
@"
# Update

`python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print("Updated title:", book.title)
# Example output:
# Updated title: Nineteen Eighty-Four


`powershell
# delete.md
@"
# Delete

`python
from bookshelf.models import Book
deleted_count, _ = Book.objects.filter(title="Nineteen Eighty-Four").delete()
print("Deleted rows:", deleted_count)
print("Remaining books:", Book.objects.count())
# Example output:
# Deleted rows: 1
# Remaining books: 0


`powershell
# CRUD_operations.md (combined)
@"
# CRUD Operations (bookshelf.Book via Django shell)

## Create
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created:", b.id, str(b))
# Created: 1 1984 by George Orwell (1949)

## Retrieve
book = Book.objects.get(id=b.id)
print("Retrieved:", book.id, book.title, book.author, book.publication_year)
# Retrieved: 1 1984 George Orwell 1949

## Update
book.title = "Nineteen Eighty-Four"
book.save()
print("Updated title:", book.title)
# Updated title: Nineteen Eighty-Four

## Delete
deleted_count, _ = Book.objects.filter(id=book.id).delete()
print("Deleted rows:", deleted_count)
print("Remaining books:", Book.objects.count())
# Deleted rows: 1
# Remaining books: 0
