"""Order admin class"""
import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    """Adding tabular to the admin"""
    model = OrderItem
    raw_id_fields = ["product"]


def export_to_csv(modeladmin, request, query_set):
    """Exporting as CSV at admin page"""
    opts = modeladmin.model._meta
    content_disposition = "attachment; filename={opts.verbose_name}.csv"
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not
              field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in query_set:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = "Export to CSV"


def order_detail(obj):
    """Adding specifics"""
    url = reverse("orders:admin_order_detail", args=[obj.id])
    return mark_safe(f"<a href = '{url}'>View</a>")


def order_pdf(obj):
    """PDF printing"""
    url = reverse("orders:admin_order_pdf", args=[obj.id])
    return mark_safe(f"<a href = '{url}'>PDF</a>")


order_pdf.short_description = "Invoice"


@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    "Admin class"
    list_display = ("user", "address", "created", "paid",
                    order_detail, order_pdf)
    list_filter = ("region", "address", "created")
    inlines = [OrderItemInline]
    actions = [export_to_csv]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product","price"]
