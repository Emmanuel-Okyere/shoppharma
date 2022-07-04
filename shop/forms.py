from django import forms

from shop.models import Product, Category
class ProductCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label ="Select",
    widget=forms.Select(attrs={"class":"form-control"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class":"form-input form"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-input form"}))

    class Meta:
        model = Product
        fields = ["category","name","description","image","price"]

class SearchForm(forms.Form):
    """Creating the search form class"""
    query = forms.CharField(label="")
