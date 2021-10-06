from .models import Order


def cart_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_item = order.get_cart_items
    else:

        order = {'get_cart_items': 0,
                 'get_cart_total': 0}
        cart_item = order['get_cart_items']
    return {'cart_item': cart_item}
