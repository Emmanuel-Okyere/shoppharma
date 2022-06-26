from django.urls import reverse
from cart.forms import CartAddProductForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from shop.api.serializer import ProductSerializer,CategorySerializer
from .models import Category, Product
from rest_framework import generics, status
from rest_framework.response import Response
from .forms import ProductCreateForm
import requests
# Create your views here.
# BASE_URL = 'http://127.0.0.1:8000/adminshop'
# r = requests.post(f'{BASE_URL}/add')
# courses = r.json()
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



class ProductPostSerializer(generics.ListAPIView):
    """Book list API View"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated, IsSuperUser)

    def post(self, request, *args, **kwargs):
        """Post method for HTTP POST request from Booklist View"""
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "details": "book added successfully",
                "data": {
                    "category": serializer.data["category"],
                    "name": serializer.data["name"],
                    "description": serializer.data["description"],
                    "price": serializer.data["price"],
                    "image": serializer.data["image"]
                }
            })
        return Response({
            "status": "failure",
            "details": serializer.errors})

class CategoryAddSerializer(generics.ListAPIView):
    """Catalogue list API View"""
    queryset = Category.objects
    serializer_class = CategorySerializer
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated, IsSuperUser)

    def post(self, request):
        """Post method for HTTP POST request from Catalogue View"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "details": "catalogue created",
                "data": {
                    "name": serializer.data["name"]
                }}, status=status.HTTP_201_CREATED)
        return Response({
            "status": "failure",
            "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

def add_product(request):
    if request.method == "POST":
        form =ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('shop:shop'))
    form = ProductCreateForm()
    return render(request, "shop/add_product.html", {"form": form})
