from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from authentications.models import Users

from authentications.forms import LoginForm, UserRegistrationForm
# Create your views here.
def user_login(request):
    """Creating the user login view"""
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            print(clean_data)
            user = authenticate(request,email_address = clean_data['email_address'],
            password = clean_data["password"])
            if user is not None:
                login(request,user)
                return redirect("shop:shop")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request,"authentications/login.html",{"form":form})

def register(request):
    """User registers view"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            clean_data  =form.cleaned_data
            print(clean_data)
            new_user = Users.objects.create_user(
                email_address = clean_data["email_address"],
                password = clean_data["password2"],
                first_name=clean_data["first_name"],
                last_name=clean_data["last_name"])
            new_user.save()
            return HttpResponse("User Registered successfully")
    else:
        form = UserRegistrationForm()
    return render(request, "authentications/register.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("shop:shop")
