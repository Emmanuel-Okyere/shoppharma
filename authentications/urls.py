
from django.urls import include, path
from . import views
urlpatterns = [
    path("register/", views.UserRegistraion.as_view(), name = "register"),
    path("login/", views.UserLogin.as_view(), name = "login"),

]