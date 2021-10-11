import json
from .models import Order


# def cookie_cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cart_item = order.get_cart_items
#     else:
#         items = []
#         try:
#             cart = json.loads(request.COOKIES['cart'])
#         except KeyError:
#             cart = {}
#         print('Cart:', cart)
#         order = {'get_cart_items': 0,
#                  'get_cart_total': 0,
#                  'shipping': False}
#         cart_item = order['get_cart_items']
#
#         for item in cart:
#             try:
#                 cart_item += cart[item]['quantity']
#                 product = Product.objects.get(id=item)
#                 total = (product.price * cart[item]['quantity'])
#
#                 order['get_cart_total'] += total
#                 order['get_cart_items'] += cart[item]['quantity']
#
#                 item = {
#                     'product':{
#                         'id': product.id,
#                         'name': product.name,
#                         'description': product.description,
#                         'price': product.price,
#                         'discount_price': product.discount_price,
#                         'image': product.image,
#                                 },
#                         'quantity': cart[item]['quantity'],
#                         'get_total': total
#                 }
#                 items.append(item)
#
#                 if not product.digital:
#                     order['shipping'] = True
#             except:
#                 pass
#
#     return {'cart_item': cart_item, 'order_obj': order, 'items_obj': items}


def cookie_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_item = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except KeyError:
            cart = {}
        print('Cart:', cart)
        order = {'get_cart_items': 0}
        cart_item = order['get_cart_items']

        for item in cart:
            cart_item += cart[item]['quantity']

    return {'cart_item': cart_item}

