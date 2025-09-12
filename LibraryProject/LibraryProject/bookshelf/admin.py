from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # columns in the list page
    list_display = ("title", "author", "publication_year")
    # right-hand filters
    list_filter = ("author", "publication_year")
    # search box (case-insensitive)
    search_fields = ("title", "author")
    # optional niceties
    ordering = ("title",)
    list_per_page = 25

