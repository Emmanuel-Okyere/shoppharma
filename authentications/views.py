from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from authentications.models import Users
from authentications.forms import LoginForm, UserRegistrationForm


# Create your views here.
def user_login(request):
    """Creating the user login view"""
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request,email_address = clean_data['email_address'],
            password = clean_data["password"])
            if user is not None:
                login(request,user)
                messages.success(request, "Login Success")
                return redirect("shop:shop")
            else:
                messages.error(request, "Invalid Credentials, Try Again")
                return render(request,"authentications/login.html",{"form":form})
    else:
        form = LoginForm()
    return render(request,"authentications/login.html",{"form":form})

def register(request):
    """User registers view"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            clean_data  =form.cleaned_data
            new_user = Users.objects.create_user(
                email_address = clean_data["email_address"],
                password = clean_data["password2"],
                first_name=clean_data["first_name"],
                last_name=clean_data["last_name"],
                phone_number = clean_data["phone_number"])
            new_user.save()
            messages.success(request, "Registration Successful, Please Login")
            return redirect("authentications:login")
    else:
        form = UserRegistrationForm()
    return render(request, "authentications/register.html", {"form": form})

def user_logout(request):
    """USer logout view"""
    logout(request)
    return redirect("shop:shop")
