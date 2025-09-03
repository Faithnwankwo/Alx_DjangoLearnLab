from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

ct = ContentType.objects.get_for_model(Book)
lib, _ = Group.objects.get_or_create(name="Librarian")
mem, _ = Group.objects.get_or_create(name="Member")

lib_perms = Permission.objects.filter(content_type=ct, codename__in=["add_book","change_book","delete_book","view_book"])
mem_perms = Permission.objects.filter(content_type=ct, codename__in=["view_book"])

lib.permissions.set(lib_perms)
mem.permissions.set(mem_perms)

print("✅ Groups configured.")
