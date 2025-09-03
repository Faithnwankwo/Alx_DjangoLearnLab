from relationship_app.models import Author, Book, Library, Librarian

# reset (dev-safe)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Authors
a1 = Author.objects.create(name="George Orwell")
a2 = Author.objects.create(name="Aldous Huxley")

# Books
b1 = Book.objects.create(title="1984", author=a1)
b2 = Book.objects.create(title="Animal Farm", author=a1)
b3 = Book.objects.create(title="Brave New World", author=a2)

# Libraries
lib1 = Library.objects.create(name="Central Library")
lib2 = Library.objects.create(name="West End Library")

# Many-to-Many links
lib1.books.add(b1, b2)
lib2.books.add(b2, b3)

# One-to-One librarians
Librarian.objects.create(name="Alice Carter", library=lib1)
Librarian.objects.create(name="Noah Singh", library=lib2)

print("✅ Seed data created.")
