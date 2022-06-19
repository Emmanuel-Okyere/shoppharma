from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger,InvalidPage
from django.urls import reverse
from .models import Product, Category
from cart.forms import CartAddProductForm

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
        products = products.filter(category=category)
    return render(request, "shop/index.html", {"category": category,
                                                      "categories": categories,
                                                      "products": products,
                                                      "post":posts,"page":page})


def product_detail(request, id, slug):
    """Product detial"""
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/details.html", {"product": product,"categories":categories,
    "cart_product_form":cart_product_form})


def page_not_found(request):
    """When payment goes through"""
    return render(request, "shop/404.html")
