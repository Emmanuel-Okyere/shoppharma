from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# import weasyprint
from .models import Order
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Braintree
import braintree
from django.conf import settings
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

# from .tasks import order_created

# Create your views here.

@login_required
def order_create(request):
    """Creating the order"""
    cart = Cart(request)
    if not request.session["cart"]:
        return redirect(reverse('cart:cart_detail'))
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item["product"], price=item["price"],
                                         quantity=item["quantity"])
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('orders:process'))
    else:
        form = OrderCreateForm()
        return render(request, "orders/checkout.html", {"cart": cart, "form": form})



def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})



def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/pdf.html", {"order": order})
    response = HttpResponse(content_type='application/pdf')
    response["Content-Disposition"] = f"filename = order_{order_id}.pdf"
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
    #     settings.STATIC_ROOT + "css/pdf.css")])
    return response
@login_required
def payment_process(request):
    """Payment view"""
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id= order_id)
    total_cost = order.get_total_cost()
    if request.method =="POST":
        nonce = request.POST.get("payment_method_nonce", None)
        result = gateway.transaction.sale({
            "amount": f"{total_cost:.2f}",
            "payment_method_nonce":nonce,
            "options":{
                "submit_for_settlement":True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            # launch asynchronous task
            # payment_completed.delay(order.id)
            return redirect("orders:done")
        else:
            return redirect("orders:canceled")
    else:
        client_token = gateway.client_token.generate()
        return render(request,"orders/payment.html", {"client_token":client_token,
        "order":order})
@login_required
def payment_done(request):
    """When payment goes through"""
    return render(request, "orders/done.html")
@login_required
def payment_canceled(request):
    """Canceled payments"""
    return render(request, "orders/canceled.html")
