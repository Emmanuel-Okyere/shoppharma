from django import forms

from shop.models import Product
class ProductCreateForm(forms.ModelForm):

    category = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-input input"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={"class":"form-input form"}))

    class Meta:
        model = Product
        fields = ["category","name","description","image","price"]
