from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Go to login or a dashboard; login makes you authenticated immediately
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
