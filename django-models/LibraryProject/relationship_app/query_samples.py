from relationship_app.models import Author, Book, Library

print("\nBooks by George Orwell:")
for b in Book.objects.filter(author__name="George Orwell"):
    print(" -", b.title)

print("\nBooks in Central Library:")
for b in Library.objects.get(name="Central Library").books.all():
    print(" -", b.title, "by", b.author.name)

print("\nLibrarian for West End Library:")
print(" -", Library.objects.get(name="West End Library").librarian.name)
