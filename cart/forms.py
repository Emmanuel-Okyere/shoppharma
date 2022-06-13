"""Forms.py"""
from django import forms
from django.utils.translation import gettext_lazy as _
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    """Adding product to cart"""
    quantity = forms.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                     label=_('Quantity'),
                                      widget=forms.Select(attrs ={"class":"form-control quantity"}))
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
