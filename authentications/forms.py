from django import forms
from authentications.models import Users
class LoginForm(forms.Form):
    """Creating the actual form field view"""
    email_address = forms.CharField(max_length=50, required=True,
    widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=50,
    widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserRegistrationForm(forms.ModelForm):
    """User registration model form"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email_address = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"form-control"}),
    label="Password")
    password2 = forms.CharField(label="Confirm Password",
    widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        """Already contained in form"""
        model = Users
        fields = ["first_name", "last_name","email_address"]

    def clean_password2(self):
        """Checking if passwords matches"""
        clean_data = self.cleaned_data
        if clean_data["password"]!=clean_data["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return clean_data["password2"]