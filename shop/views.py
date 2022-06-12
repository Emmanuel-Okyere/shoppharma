from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request, category_slug=None):
    """Products list view"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "shop/index.html", {"category": category,
                                                      "categories": categories, "products": products})


def product_detail(request, id, slug):
    """Product detial"""
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/details.html", {"product": product,"categories":categories,
    "cart_product_form":cart_product_form})