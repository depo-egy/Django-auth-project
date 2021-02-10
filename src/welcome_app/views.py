from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.urls import reverse
from welcome_app.forms import CustomUserCreationForm

# Create your views here.

def welcome(request):
    return render(request , "welcome_app/home.html" , {})


def register(request):
    if request.method == "GET":
        return render(request, "welcome_app/register.html",
            {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user = form.save()
            #login(request, user)
    return redirect(reverse("welcome")) #view function