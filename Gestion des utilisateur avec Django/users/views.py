from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
# Create your views here.


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            user = authenticate(request, username=username1, password=password1)
            print("2ddff")
            form.save()
            if user is not None:
                login(request, user)
                return redirect(reverse("dashboard"))