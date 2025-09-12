from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Profile", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_of_birth")
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Profile", {"classes": ("wide",), "fields": ("date_of_birth", "profile_photo")}),
    )
