from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

def user_profile_upload_to(instance, filename):
    # Files will be stored like: media/profile_photos/<username>/<filename>
    return f"profile_photos/{instance.username}/{filename}"

class CustomUserManager(UserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        # Accepts extra fields like date_of_birth, profile_photo
        return super().create_user(username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return super().create_superuser(username, email=email, password=password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to=user_profile_upload_to, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
