import datetime
import weasyprint
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views import View
from shop import settings
from .forms import ProductForm
from .models import Product, Order, OrderItem, ShippingAddress
from .utils import cart_data, guest_order
from django.core.mail import send_mail


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class ProductsView(View):

    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            products = Product.objects.filter(Q(name__icontains=search) |
                                              Q(producer__icontains=search))
        else:
            products = Product.objects.all().order_by('-id')
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'products.html', {'page_obj': page_obj,
                                                 'search': search})


class ProductView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        products = Product.objects.filter(producer__icontains=product.producer)
        return render(request, 'product.html', {'product': product,
                                                'products': products})


class AddProductView(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Dodaj'})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('name_app:products')
        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Dodaj'})


class EditProductView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(instance=product)
        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Edytuj'})

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('name_app:product', product_id=product.id)
        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Edytuj'})


class DeleteProductView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'del_confirm.html', {'product': product})

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('name_app:index')


class CartView(View):

    def get(self, request):
        data = cart_data(request)
        order = data['order']
        items = data['items']
        return render(request, 'cart.html', {'items': items,
                                             'order': order,
                                             'shipping': False})


class CheckoutView(View):

    def get(self, request):
        data = cart_data(request)
        order = data['order']
        items = data['items']
        return render(request, 'checkout.html', {'items': items,
                                                 'order': order})


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('produtId:', productId)

    customer = request.user.customer
    product = get_object_or_404(Product, id=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('Item was added', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
    else:
        customer, order = guest_order(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            first_name=data['shipping']['first_name'],
            last_name=data['shipping']['last_name'],
            company=data['shipping']['company'],
            address=data['shipping']['address'],
            postcode=data['shipping']['postcode'],
            city=data['shipping']['city'],
        )

    order_confirmation(request, order, customer)
    return JsonResponse('Payment submitted..', safe=False)


def order_confirmation(request, order, customer):
    template = render_to_string('send_mail.html', {'customer': customer,
                                                   'order': order})
    mail_sent = send_mail(
        f'Potwierdzenie zamowienia nr.{order.transaction_id}',
        template,
        settings.DEFAULT_FROM_EMAIL,
        [customer.email],
        fail_silently=False,
    )
    return mail_sent


def invoice_pdf(request, shipping_address_id):
    shipping_address = get_object_or_404(ShippingAddress, id=shipping_address_id)
    html = render_to_string('invoice.html',
                            {'shipping_address': shipping_address})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=zamowienie_{shipping_address.order.transaction_id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(
                                               settings.STATIC_ROOT + 'css/invoice.css')])
    return response
