from bookshelf.models import Book
book = Book.objects.get(id=1)  # use the id printed during Create
book.id
book.title
book.author
book.publication_year
# Expected example lines:
# 1
# 1984
# George Orwell
# 1949
