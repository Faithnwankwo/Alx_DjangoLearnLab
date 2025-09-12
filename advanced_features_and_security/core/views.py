from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse("Welcome to the dashboard.")

@permission_required("auth.change_user", raise_exception=True)
def manage_users(request):
    return HttpResponse("You can change users because you have auth.change_user.")
