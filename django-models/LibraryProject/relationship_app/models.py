from django.db import models
from django.contrib.auth.models import User

# --- Existing models kept so earlier tasks still pass ---
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    def __str__(self): return f"{self.title} ({self.author.name})"

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries", blank=True)
    def __str__(self): return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")
    def __str__(self): return f"{self.name} @ {self.library.name}"

# --- New for Task 3 ---
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("LIBRARIAN", "Librarian"),
        ("MEMBER", "Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="MEMBER")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
