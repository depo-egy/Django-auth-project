from django.urls import path , include
from .views import welcome ,register
from django.contrib.auth import views as auth_views

urlpatterns = [
path("", welcome, name="welcome"),
path('accounts/', include("django.contrib.auth.urls")),
path("register/", register, name="register"),

   

]

