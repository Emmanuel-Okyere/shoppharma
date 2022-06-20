
from django.urls import include, path
from shop import views

app_name = "shop"
urlpatterns = [
    path("shop/", views.product_list, name = "shop"),
    path("shop/<slug:category_slug>/", views.product_list, name = "product_list_by_category"),
    path("<int:id>/<slug:slug>/detail/", views.product_detail, name = "product_detail"),
]