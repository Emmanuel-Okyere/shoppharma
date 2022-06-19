from atexit import register
from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    """Adding tabular to the admin"""
    model = OrderItem
    raw_id_fields = ["product"]
    
@admin.register(Order)
class OrderAdminClass(admin.ModelAdmin):
    list_display = ["first_name","email_address","created"]
    list_filter = ("region", "email_address", "created")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product","price"]