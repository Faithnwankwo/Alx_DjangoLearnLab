from bookshelf.models import Book
book = Book.objects.get(id=1)  # use the id you created
book.id
book.title
book.author
book.publication_year
