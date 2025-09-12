from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

