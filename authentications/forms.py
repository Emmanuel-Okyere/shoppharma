from django import forms
from authentications.models import Users
class RegisterUser(forms.ModelForm):
    """User registration form"""
    class Meta:
        model = Users
        fields = ["first_name","last_name","email_address","password"]


class LoginUSer(forms.ModelForm):
    """User login"""
    class Meta:
        model = Users
        fields = ["email_address","password"]
