# run.ps1  — sample actions for your project
$proj = "$env:USERPROFILE\Alx_DjangoLearnLab\Introduction_to_Django\LibraryProject"
Set-Location $proj

# Add a few sample books (safe to run multiple times)
& "$env:USERPROFILE\Alx_DjangoLearnLab\Introduction_to_Django\.venv\Scripts\python.exe" manage.py shell -c "from catalog.models import Book; Book.objects.get_or_create(title='Things Fall Apart', author='Chinua Achebe'); Book.objects.get_or_create(title='Half of a Yellow Sun', author='Chimamanda Ngozi Adichie'); Book.objects.get_or_create(title='The Alchemist', author='Paulo Coelho')"

# Start the dev server
& "$env:USERPROFILE\Alx_DjangoLearnLab\Introduction_to_Django\.venv\Scripts\python.exe" manage.py runserver 8000
