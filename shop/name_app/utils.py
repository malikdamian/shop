import json
from .models import Order, Product, Customer, OrderItem


def cookie_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_item = order.get_cart_items
    else:
        items = []
        try:
            cart = json.loads(request.COOKIES['cart'])
        except KeyError:
            cart = {}
        print('Cart:', cart)
        order = {'get_cart_items': 0,
                 'get_cart_total': 0,
                 'shipping': False}
        cart_item = order['get_cart_items']

        for item in cart:
            try:
                cart_item += cart[item]['quantity']
                product = Product.objects.get(id=item)
                total = (product.price * cart[item]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_items'] += cart[item]['quantity']

                item = {
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'price': product.price,
                        'discount_price': product.discount_price,
                        'image': product.image,
                    },
                    'quantity': cart[item]['quantity'],
                    'get_total': total
                }
                items.append(item)

                if not product.digital:
                    order['shipping'] = True
            except:
                pass

    return {'cart_item': cart_item, 'order': order, 'items': items}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        cookie_data = cookie_cart(request)
        order = cookie_data['order']
        items = cookie_data['items']
    return {'order': order, 'items': items}


def guest_order(request, data):
    print('User is not logged in..')

    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookie_data = cookie_cart(request)
    items = cookie_data['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(customer=customer,
                                 complete=False
                                 )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        order_item = OrderItem.objects.create(product=product,
                                              order=order,
                                              quantity=item['quantity'])
    return customer, order
