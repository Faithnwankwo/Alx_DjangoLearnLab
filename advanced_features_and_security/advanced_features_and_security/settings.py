# settings.py for advanced_features_and_security
# ----------------------------------------------
from pathlib import Path
import os

# BASE_DIR points to: C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security
BASE_DIR = Path(__file__).resolve().parent.parent

# Replace with your existing secret key if you have one already
SECRET_KEY = "PASTE-YOUR-EXISTING-SECRET-KEY-HERE"

# Development settings
DEBUG = True
ALLOWED_HOSTS: list[str] = []

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Your custom app (must be plural: users)
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "advanced_features_and_security.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "advanced_features_and_security.wsgi.application"

# Database (SQLite by default)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"  # change to "America/Regina" if you prefer
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"
from pathlib import Path  # already at top of file, ok if duplicated import removed
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (for profile photos)
MEDIA_URL = "/media/"
import os
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Use your custom user model
AUTH_USER_MODEL = "users.CustomUser"

# Use console backend so password reset "emails" appear in the terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Tell Django where our templates live (project-level templates folder)
from pathlib import Path
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]
