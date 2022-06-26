from django import forms

from orders.models import Order
class OrderCreateForm(forms.ModelForm):
    regions = ["Greater Accra", "Central","Ahafo","Upper West",
    "Northern","Savannah","North-East","Upper East","Bono East","Brong Ahafo",
    "Oti","Volta","Eastern","Western","Western North","Ashanti"]
    choices = [(i, str(i)) for i in regions]
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input input"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    email_address = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-input form"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    region = forms.ChoiceField(choices=sorted(choices),
    widget=forms.Select(attrs={"class":"form-control"}))

    class Meta:
        model = Order
        fields = ["first_name","last_name","telephone","email_address","address","postal_code","region"]