from cart.forms import CartAddProductForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product

# Create your views here.

def product_list(request, category_slug=None):
    """Products list view"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, 9)
        try:
            posts = paginator.page(1)
        except PageNotAnInteger:
            return paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    return render(request, "shop/index.html", {"category": category,
                                                      "categories": categories,
                                                      "post":posts,"page":page})

def product_detail(request, id, slug):
    """Product detial"""
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/details.html", {"product": product,"categories":categories,
    "cart_product_form":cart_product_form})
