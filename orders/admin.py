from atexit import register
from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdminClass(admin.ModelAdmin):
    list_display = ["first_name","email_address","created"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product","price"]