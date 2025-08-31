# CRUD Operations (bookshelf.Book via Django shell)

from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b.id
str(b)

book = Book.objects.get(id=b.id)
book.id
book.title
book.author
book.publication_year

book.title = "Nineteen Eighty-Four"
book.save()
book.title

Book.objects.filter(id=book.id).delete()
Book.objects.count()
