class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.author.name})"

    # ↓ Add this block INSIDE the Book class (indent matters)
    class Meta:
        permissions = (
            ("canaddbook", "Can add book"),
            ("canchangebook", "Can change book"),
            ("candeletebook", "Can delete book"),
        )
